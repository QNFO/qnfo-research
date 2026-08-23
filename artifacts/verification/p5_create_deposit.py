#!/usr/bin/env python3
"""P5: create Zenodo deposit (wrapped metadata per ZENODO-DEPOSIT-CREATE-SHAPE-1).
NOTE: related_identifiers triggers 500 on deposit POST/PUT (verified RES.022
P6) — GitHub provenance goes in the README instead."""
import json
import sys
import urllib.request

TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
OUT = sys.argv[1] if len(sys.argv) > 1 else "artifacts/verification/p5_deposit.json"

metadata = {
    "title": "The Ultrametric Program: One Structural Object Across Seven Research Domains, and Its Falsifiable Tests",
    "description": (
        "Seven research domains — ultrametric physics, the laws of form, infomatics, "
        "paradigm engineering, consilience research, a cloud-native platform, and "
        "interactive demos — are claimed to be seven vocabularies for one structural "
        "object: a nested, hierarchical partition logic. The object is defined by the "
        "ultrametric inequality and its strict hierarchy of nested balls; the specific "
        "arithmetic — p-adic valuation, the adelic product formula — is one realization, "
        "the hierarchy is the invariant. This paper states that thesis plainly and makes "
        "it testable. The program's scientific content is carried by three falsifiable "
        "hypotheses: H1, that ultrametric structure is an effective compression and "
        "clustering prior for high-dimensional sparse measurement data; H2, that "
        "continuous Archimedean physics appears as the thermodynamic or ergodic average "
        "over the leaves of the ultrametric hierarchy; and H3, that quantum-coherent "
        "systems under structured hierarchical noise exhibit decoherence scaling that "
        "deviates from the standard Markovian prediction in a p-adic pattern. The strong "
        "form of the program is bound to a 2028 decision point. The program serves a "
        "mission — an energy-efficiency benchmark for quantum computing (joules per "
        "correct solution) — to which the thermodynamic bounds of computation are the "
        "direct link. Evidence from the program's own corpus is presented where it "
        "exists, including a computational audit of the keyword taxonomy that shows the "
        "consilience is semantic rather than lexical, and a deterministic verification "
        "suite whose numbers are reproduced exactly by the deposited scripts. The paper "
        "also confronts the program's deepest open questions: the observer's resolution "
        "hierarchy, the global topology of the tree, and whether the unity is one radix "
        "or a family of incommensurable grammars."
    ),
    "upload_type": "publication",
    "publication_type": "preprint",
    "creators": [
        {"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO",
         "orcid": "0009-0002-4317-5604"}
    ],
    "license": "CC-BY-4.0",
    "access_right": "open",
    "keywords": ["ultrametric", "p-adic", "adelic", "laws of form", "resolution hierarchy",
                 "compression prior", "Archimedean emergence", "energy benchmark",
                 "joules-per-solution", "measurement", "consilience"],
    "version": "v1.0",
}

body = json.dumps({"metadata": metadata}).encode("utf-8")
url = "https://zenodo.org/api/deposit/depositions?access_token=" + TOKEN
req = urllib.request.Request(url, data=body, method="POST",
                             headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        resp = json.loads(r.read().decode())
    print("STATUS:", r.status)
    print("DEPOSIT_ID:", resp.get("id"))
    print("CONCEPTRECID:", resp.get("conceptrecid"))
    print("DOI:", resp.get("doi"))
    print("LINKS:", {k: v for k, v in resp.get("links", {}).items() if k in ("bucket", "self", "publish")})
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resp, f, indent=2)
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code, e.read().decode()[:2000])
    sys.exit(1)
