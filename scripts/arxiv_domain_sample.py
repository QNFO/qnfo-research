#!/usr/bin/env python3
"""arxiv_domain_sample.py — collect recent arXiv abstracts per category and
extract a per-domain keyword vocabulary.

Pipeline (deterministic; no randomness):
  1. For each category: query export.arxiv.org (Atom), sorted by submittedDate
     descending, max_results=N (browser-like User-Agent).
  2. Normalize title+abstract text (lowercase, strip LaTeX braces, collapse
     whitespace).
  3. Vocabulary extraction per category — BIGRAM ONLY:
     Technical terms in modern science are overwhelmingly compound
     ('phase-transition', 'neural-network', 'monte-carlo', 'p-adic'); single
     tokens ('energy', 'field', 'model') are too ambiguous to discriminate
     domains. This mirrors the QNFO canonical taxonomy, whose keywords are
     likewise compound technical terms.
       tokens  = words (alpha/hyphen), stopwords + numbers + single letters
                 removed, length >= 3
       bigrams = adjacent content-bearing token pairs (a-b)
       terms   = bigrams occurring >= min_freq times in the sample
       ranking = term frequency (desc), then lexical order (deterministic)
       vocabulary = top-K terms by that ranking
  4. Write:
       artifacts/external-search/arxiv_raw_<date>.json   (full evidence)
       artifacts/external-search/arxiv_domains.json      (domains JSON for
                                                          terminology_silos.py)
"""
import datetime as _dt
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

CATEGORIES = {
    "quant-ph": "Quantum Physics",
    "math.NT": "Number Theory",
    "cs.LG": "Machine Learning",
    "q-bio.GN": "Genomics",
    "cond-mat.mtrl-sci": "Materials Science",
    "econ.TH": "Economic Theory",
}
MAX_ABSTRACTS = 40
TOP_K = 80
MIN_FREQ = 2
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
NS = {"a": "http://www.w3.org/2005/Atom"}

STOPWORDS = {
    # standard English function words
    "a", "an", "the", "and", "or", "of", "to", "in", "for", "on", "with",
    "we", "our", "this", "that", "these", "those", "is", "are", "was", "were",
    "be", "been", "being", "as", "at", "by", "from", "has", "have", "had",
    "it", "its", "their", "they", "them", "he", "she", "his", "her",
    "not", "no", "but", "if", "then", "than", "so", "such", "can", "may",
    "will", "would", "should", "could", "also", "very", "much", "many",
    "more", "most", "some", "any", "all", "each", "both", "new", "recent",
    "study", "studies", "results", "result", "show", "shows", "shown",
    "using", "use", "used", "based", "paper", "work", "approach", "method",
    "methods", "proposed", "propose", "introduce", "introduced", "however",
    "while", "which", "who", "whom", "when", "where", "how", "what", "why",
    "between", "among", "over", "under", "through", "into", "out", "up",
    "down", "first", "second", "third", "one", "two", "three", "four", "five",
    "well", "also", "within", "without", "via", "per", "et", "al", "doi",
    "eg", "ie", "etc", "cf", "figure", "fig", "table", "section", "see",
    "dataset", "data", "experiment", "experiments", "experimental",
    "theoretical", "provide", "provides", "present", "presents", "we",
    "our", "newly", "often", "typically", "generally", "significant",
    "significantly", "better", "best", "improved", "improves", "improve",
    # expanded function words
    "about", "above", "after", "again", "against", "before", "behind",
    "below", "beside", "beyond", "both", "during", "each", "few", "further",
    "hence", "here", "hereby", "herein", "however", "indeed", "itself",
    "just", "least", "less", "like", "likely", "mainly", "might",
    "moreover", "mostly", "must", "namely", "neither", "never",
    "nevertheless", "next", "nonetheless", "nor", "nothing", "now",
    "once", "only", "onto", "otherwise", "ours", "ourselves",
    "overall", "particularly", "perhaps", "rather", "regarding",
    "several", "shall", "since", "still", "there", "thereby",
    "therefore", "thus", "together", "toward", "towards",
    "unless", "upon", "usually", "versus", "vs", "whether",
    "yet", "you", "your", "yours", "yourself",
    # generic science shell words (non-technical in any domain)
    "field", "fields", "framework", "frameworks", "structure", "structures",
    "number", "numbers", "local", "global", "general", "generalized",
    "specific", "particular", "simple", "complex", "large", "small",
    "high", "low", "higher", "lower", "good", "poor", "strong", "weak",
    "different", "various", "multiple", "single", "dual",
    "main", "major", "minor", "key", "core", "central", "important",
    "relevant", "useful", "efficient", "effective", "possible", "potential",
    "previous", "prior", "current", "existing", "following", "above",
    "below", "given", "known", "unknown", "observed", "obtained",
    "performed", "conducted", "compared", "discussed", "described",
    "analyzed", "evaluated", "examined", "tested", "consider", "considered",
    "require", "required", "allows", "enables", "allowing", "enabling",
    "involves", "involve", "includes", "include", "consists", "consist",
    "corresponds", "corresponding", "associated", "related", "relating",
    "regarding", "concerning", "depending", "according", "follows",
    "follow", "appear", "appears", "seems", "seem", "tend", "tends",
    "helps", "help", "aims", "aim", "goal", "purpose", "objective",
    "task", "tasks", "problem", "problems", "question", "questions",
    "issue", "issues", "challenge", "challenges", "example", "examples",
    "case", "cases", "part", "parts", "aspect", "aspects", "component",
    "components", "feature", "features", "property", "properties",
    "behavior", "behaviour", "characteristic", "characteristics",
    "condition", "conditions", "context", "contexts", "range", "ranges",
    "level", "levels", "degree", "extent", "way", "ways", "kind", "kinds",
    "type", "types", "form", "forms", "role", "roles", "function",
    "functions", "process", "processes", "step", "steps", "stage",
    "stages", "phase", "phases", "mechanism", "mechanisms", "pattern",
    "patterns", "trend", "trends", "source", "sources", "area", "areas",
    "domain", "domains", "category", "categories", "class", "classes",
    "group", "groups", "set", "sets", "subset", "subsets", "sequence",
    "sequences", "order", "orders", "point", "points", "value", "values",
    "term", "terms", "definition", "definitions", "concept", "concepts",
    "notion", "notions", "idea", "ideas", "view", "views", "perspective",
    "perspectives", "dimension", "dimensions", "direction", "directions",
    "criterion", "criteria", "factor", "factors", "parameter", "parameters",
    "variable", "variables", "measure", "measures", "measurement",
    "measurements", "quantity", "quantities", "amount", "amounts", "size",
    "sizes", "length", "width", "height", "depth", "weight", "mass",
    "speed", "rate", "rates", "frequency", "frequencies", "intensity",
    "density", "temperature", "pressure", "volume", "energy", "power",
    "time", "times", "space", "spaces", "region", "regions", "location",
    "locations", "position", "positions", "state", "states", "status",
    "change", "changes", "changed", "increase", "increases", "increased",
    "decrease", "decreases", "decreased", "reduce", "reduces", "reduced",
    "enhance", "enhances", "enhanced", "improve", "improves", "improved",
    "develop", "develops", "developed", "development", "design", "designs",
    "designed", "implement", "implements", "implemented", "implementation",
    "construct", "constructs", "constructed", "construction", "build",
    "builds", "built", "create", "creates", "created", "creation",
    "generate", "generates", "generated", "generation", "produce",
    "produces", "produced", "production", "obtain", "obtains", "obtained",
    "find", "finds", "found", "finding", "findings", "report", "reports",
    "reported", "identify", "identifies", "identified", "identification",
    "detect", "detects", "detected", "detection", "estimate", "estimates",
    "estimated", "estimation", "predict", "predicts", "predicted",
    "prediction", "predictions", "compare", "compares", "compared",
    "comparison", "contrast", "distinguish", "distinguishes",
    "distinguished", "separate", "separates", "separated", "combine",
    "combines", "combined", "combination", "interaction", "interactions",
    "relation", "relations", "relationship", "relationships", "connection",
    "connections", "link", "links", "linked", "coupling", "coupled",
    "dependence", "dependent", "independent", "independence", "variation",
    "variations", "vary", "varies", "varying", "distribution",
    "distributions", "average", "mean", "median", "standard", "deviation",
    "error", "errors", "uncertainty", "uncertainties", "confidence",
    "accuracy", "precision", "sensitivity", "robustness", "reliability",
    "validity", "quality", "efficiency", "effectiveness", "performance",
    "capacity", "capability", "capabilities", "advantage", "advantages",
    "disadvantage", "disadvantages", "benefit", "benefits", "cost",
    "costs", "tradeoff", "tradeoffs", "limitation", "limitations",
    "drawback", "drawbacks", "concern", "concerns", "difficulty",
    "difficulties", "complexity", "complexities", "simplicity",
    "flexibility", "versatility", "utility", "applicability", "relevance",
    "significance", "importance", "implication", "implications",
    "consequence", "consequences", "impact", "influence", "influences",
    "effect", "effects", "affect", "affects", "affecting", "contribute",
    "contributes", "contributed", "contribution", "contributions",
    "support", "supports", "supported", "evidence", "suggest", "suggests",
    "suggested", "suggestion", "suggestions", "indicate", "indicates",
    "indicated", "indication", "demonstrate", "demonstrates",
    "demonstrated", "demonstration", "validate", "validates", "validated",
    "validation", "confirm", "confirms", "confirmed", "confirmation",
    "verify", "verifies", "verified", "verification", "check", "checks",
    "checked", "examine", "examines", "examined", "explore", "explores",
    "explored", "exploration", "investigate", "investigates",
    "investigated", "investigation", "analyze", "analyzes", "analyzed",
    "analysis", "analyses", "evaluate", "evaluates", "evaluated",
    "evaluation", "assess", "assesses", "assessed", "assessment",
    "review", "reviews", "reviewed", "discuss", "discusses", "discussed",
    "discussion", "discussions", "address", "addresses", "addressed",
    "highlight", "highlights", "highlighted", "emphasize", "emphasizes",
    "emphasized", "stress", "stresses", "stressed", "note", "notes",
    "noted", "remark", "remarks", "notably", "especially", "specifically",
    "generally", "typically", "commonly", "frequently", "rarely",
    "theory", "theories", "history", "future", "foundation", "foundations",
    "statement", "statements", "constructive", "thesis", "survey",
    "introduction", "towards", "framework", "perspective", "perspectives",
    "seldom", "almost", "nearly", "approximately", "roughly", "exactly",
    "precisely", "certainly", "definitely", "probably", "possibly",
    "perhaps", "maybe", "apparently", "evidently", "presumably",
    "respectively", "correspondingly", "accordingly", "consequently",
    "therefore", "thus", "hence", "thereby", "thereafter", "meanwhile",
    "simultaneously", "subsequently", "previously", "afterwards",
    "beforehand", "earlier", "later", "latter", "former", "following",
    "preceding", "subsequent", "ensuing", "resulting", "resultant",
    "consequent", "eventual", "ultimate", "final", "initial",
    "intermediate", "transient", "temporary", "permanent", "persistent",
    "continuous", "continual", "constant", "stable", "steady", "gradual",
    "abrupt", "sudden", "rapid", "swift", "slow", "moderate",
    "considerable", "substantial", "significant", "insignificant",
    "negligible", "minimal", "marginal", "slight", "subtle", "noticeable",
    "observable", "visible", "apparent", "evident", "obvious", "clear",
    "unclear", "ambiguous", "vague", "precise", "accurate", "exact",
    "correct", "incorrect", "right", "wrong", "true", "false", "valid",
    "invalid", "sound", "unsound", "solid", "rigorous", "strict", "formal",
    "informal", "intuitive", "heuristic", "pragmatic", "practical",
    "applied", "fundamental", "basic", "advanced", "sophisticated",
    "novel", "original", "innovative", "creative", "conventional",
    "traditional", "standard", "typical", "usual", "normal", "regular",
    "routine", "common", "uncommon", "rare", "unique", "distinct",
    "distinctive", "special", "particular", "specific", "generic",
    "universal", "global", "local", "regional", "cross", "multi", "inter",
    "intra", "sub", "super", "hyper", "ultra", "extra", "meta", "quasi",
    "semi", "pseudo", "proto", "counter", "anti", "pro", "co", "de",
    "re", "pre", "post", "non", "un", "in", "im", "il", "ir", "dis",
    "mis", "over", "under", "out", "off", "at", "by", "for", "with",
    "from", "into", "onto", "upon", "through", "across", "along", "around",
    "behind", "beneath", "beside", "beyond", "inside", "outside",
    "within", "without", "during", "after", "before", "since", "until",
    "till", "between", "among", "amongst", "amid", "amidst", "throughout",
    "against", "towards", "toward", "unto", "via", "per", "versus", "vs",
    "plus", "minus", "times", "divided", "multiplied", "equals", "equal",
    "equivalent", "identical", "similar", "different", "dissimilar",
    "comparable", "parallel", "analogous", "corresponding", "matching",
    "mismatched", "consistent", "inconsistent", "compatible",
    "incompatible", "coherent", "incoherent", "logical", "illogical",
    "rational", "irrational", "reasonable", "unreasonable", "sensible",
    "absurd", "plausible", "implausible", "credible", "incredible",
    "believable", "unbelievable", "convincing", "unconvincing",
    "compelling", "persuasive", "influential", "powerful", "weak",
    "strong", "robust", "fragile", "stable", "unstable", "balanced",
    "unbalanced", "symmetric", "asymmetric", "uniform", "nonuniform",
    "homogeneous", "heterogeneous", "isotropic", "anisotropic",
    "linear", "nonlinear", "convex", "concave", "smooth", "rough",
    "continuous", "discontinuous", "discrete", "finite", "infinite",
    "bounded", "unbounded", "compact", "dense", "sparse", "empty",
    "nonempty", "null", "zero", "nonzero", "positive", "negative",
    "neutral", "absolute", "relative", "approximate", "exact",
    "statistical", "deterministic", "probabilistic", "stochastic",
    "random", "chaotic", "periodic", "aperiodic", "oscillatory",
    "monotonic", "nonmonotonic", "asymptotic", "exponential",
    "logarithmic", "polynomial", "quadratic", "cubic",
    "bilinear", "multilinear", "tensor", "scalar", "vector",
    "matrix", "matrices", "dimensional", "dimensionless", "spatial",
    "temporal", "spatiotemporal", "geometric", "geometrical", "topological",
    "algebraic", "arithmetic", "analytic", "numerical", "symbolic",
    "computational", "algorithmic", "procedural", "declarative",
    "functional", "imperative", "concurrent", "parallel",
    "sequential", "distributed", "centralized", "decentralized",
    "hierarchical", "flat", "nested", "recursive", "iterative",
    "incremental", "adaptive", "dynamic", "static", "online", "offline",
    "realtime", "batch", "streaming", "interactive", "automated",
    "automatic", "manual", "semiautomatic", "supervised", "unsupervised",
    "reinforcement", "active", "passive", "implicit", "explicit",
    "latent", "hidden", "observed", "unobserved", "measured",
    "unmeasured", "estimated", "unestimated", "known", "unknown",
    "given", "specified", "unspecified", "parameterized",
    "nonparameterized", "normalized", "unnormalized", "standardized",
    "scaled", "rescaled", "regularized", "penalized", "constrained",
    "unconstrained", "restricted", "unrestricted", "limited", "unlimited",
    "approximated", "inexact", "imprecise", "inaccurate", "proper",
    "improper", "appropriate", "inappropriate", "suitable", "unsuitable",
    "adequate", "inadequate", "sufficient", "insufficient", "necessary",
    "unnecessary", "essential", "nonessential", "crucial", "critical",
    "vital", "important", "unimportant", "major", "minor", "primary",
    "secondary", "tertiary", "main", "principal", "auxiliary",
    "ancillary", "supplementary", "additional", "extra", "further",
    "furthermore", "moreover", "besides", "additionally", "too",
    "likewise", "similarly", "conversely", "inversely", "alternatively",
    "otherwise", "instead", "rather", "preferably", "optimally",
    "ideally", "normally", "broadly", "narrowly", "especially",
    "importantly", "considerably", "substantially", "largely", "mostly",
    "mainly", "primarily", "principally", "chiefly", "predominantly",
    "overwhelmingly", "widely", "extensively", "occasionally",
    "infrequently", "never", "always", "usually", "normally",
    "generally", "predominantly", "particularly", "notably",
}

NUM_RE = re.compile(r"^\d+$")
LETTER_RE = re.compile(r"^[a-z]$")
LATEX = re.compile(r"\\[a-zA-Z]+|\$|[{}$\\]|\\left|\\right")
PUNCT = re.compile(r"[^a-z0-9\-\s]")
WS = re.compile(r"\s+")


def normalize(text: str) -> str:
    t = text.lower()
    t = LATEX.sub(" ", t)
    t = PUNCT.sub(" ", t)
    t = WS.sub(" ", t)
    return t.strip()


def tokenize(text: str) -> list[str]:
    out = []
    for w in text.split():
        if w in STOPWORDS or NUM_RE.match(w) or LETTER_RE.match(w):
            continue
        if len(w) < 3:
            continue
        out.append(w)
    return out


def extract_vocab(texts: list[str], top_k: int, min_freq: int) -> list[str]:
    """Bigram-only vocabulary extraction (deterministic)."""
    bi: Counter = Counter()
    for txt in texts:
        toks = tokenize(normalize(txt))
        bi.update(f"{a}-{b}" for a, b in zip(toks, toks[1:]))
    freq = Counter({t: c for t, c in bi.items() if c >= min_freq})
    ranked = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [t for t, _ in ranked[:top_k]]


def fetch_category(cat: str, max_results: int) -> list[dict]:
    url = ("http://export.arxiv.org/api/query?"
           f"search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending"
           f"&max_results={max_results}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        xml = resp.read().decode("utf-8", errors="replace")
    root = ET.fromstring(xml)
    papers = []
    for entry in root.findall("a:entry", NS):
        title = (entry.findtext("a:title", "", NS) or "").strip()
        summary = (entry.findtext("a:summary", "", NS) or "").strip()
        eid = (entry.findtext("a:id", "", NS) or "").rsplit("/", 1)[-1]
        papers.append({"arxiv_id": eid, "title": title, "abstract": summary})
    return papers


def main() -> int:
    max_abs = int(sys.argv[1]) if len(sys.argv) > 1 else MAX_ABSTRACTS
    date = _dt.date.today().isoformat()
    raw_path = Path(f"artifacts/external-search/arxiv_raw_{date}.json")

    all_papers: dict[str, list[dict]] = {}
    domains: dict[str, list[str]] = {}
    for cat, label in CATEGORIES.items():
        print(f"fetching {cat} ({label}) ...", flush=True)
        for attempt in range(3):
            try:
                papers = fetch_category(cat, max_abs)
                break
            except Exception as exc:  # noqa: BLE001
                print(f"  attempt {attempt + 1} failed: {exc}", flush=True)
                time.sleep(3)
        else:
            print(f"  FAILED to fetch {cat}", flush=True)
            continue
        all_papers[cat] = papers
        texts = [f"{p['title']} {p['abstract']}" for p in papers]
        domains[cat] = extract_vocab(texts, top_k=TOP_K, min_freq=MIN_FREQ)
        print(f"  {len(papers)} papers, {len(domains[cat])} vocabulary terms",
              flush=True)
        time.sleep(3.0)  # arXiv ~3s politeness between requests

    evidence = {
        "fetched_at": date,
        "max_abstracts_per_category": max_abs,
        "categories": CATEGORIES,
        "papers": all_papers,
    }
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(json.dumps(evidence, indent=1), encoding="utf-8")

    out = {
        "domains": domains,
        "general_families": [
            # structurally general METHOD/PATTERN vocabulary (bigrams that
            # plausibly travel across fields): tools, techniques, and
            # cross-cutting patterns — the class H-SILO-2 predicts bridges
            # are drawn from.
            "machine-learning", "deep-learning", "neural-network",
            "language-model", "language-models", "foundation-model",
            "foundation-models", "reinforcement-learning", "transfer-learning",
            "semi-supervised", "self-supervised", "supervised-learning",
            "unsupervised-learning", "generative-model", "diffusion-model",
            "representation-learning", "feature-extraction", "gradient-descent",
            "stochastic-gradient", "bayesian-inference", "bayesian-optimization",
            "monte-carlo", "markov-chain", "random-walk", "stochastic-process",
            "dynamical-system", "time-series", "causal-inference", "game-theory",
            "mechanism-design", "decision-making", "social-learning",
            "information-theory", "mutual-information", "upper-bound",
            "lower-bound", "dimensionality-reduction", "principal-component",
            "singular-value", "data-driven", "model-based", "model-free",
            "black-box", "end-to-end", "benchmark", "evaluation", "forecasting",
            "phase-transition", "symmetry-breaking", "critical-exponent",
            "universality", "renormalization", "coarse-graining",
            "effective-theory", "power-law", "heavy-tail", "network-analysis",
            "community-detection", "graph-theory", "optimization-problem",
            "approximation", "estimation", "classification", "clustering",
            "regression", "prediction", "generalization", "robustness",
            "interpretability", "scaling-law", "attention-mechanism",
            "transformer", "embedding", "generative", "sampling",
        ],
        "source": f"arXiv API sample {date}, categories "
                  f"{', '.join(CATEGORIES)}, top-{TOP_K} bigrams, min_freq={MIN_FREQ}",
        "evidence_file": str(raw_path),
    }
    out_path = Path("artifacts/external-search/arxiv_domains.json")
    out_path.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"WROTE: {raw_path}")
    print(f"WROTE: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
