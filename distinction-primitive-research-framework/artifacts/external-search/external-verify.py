"""external-verify.py — external prior-art verification for the DPRF Phase 1 sweep (2026-08-29).
Queries OpenAlex + Crossref + arXiv for the boundary-rule and primon-gas prior art named in
UIA Q8. Polite pool (mailto, ~0.4s spacing), retries, evidence saved to
artifacts/external-search/external-verification-dprf-2026-08-29.json.
"""
import json, os, time, urllib.request, urllib.parse, re

OUT = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework\artifacts\external-search\external-verification-dprf-2026-08-29.json"
UA = {"User-Agent": "QNFO-research/1.0 (mailto:rowan.quni@qnfo.org)"}
MAIL = "rowan.quni@qnfo.org"

QUERIES = [
    ("korzybski-map-territory", "map is not the territory Korzybski Science and Sanity"),
    ("hartmann-levels-reality", "levels of reality ontology Nicolai Hartmann emergence"),
    ("ontic-structural-realism", "ontic structural realism Ladyman Ross Every Thing Must Go"),
    ("julia-statistical-theory-numbers", "Julia statistical theory of numbers Riemann gas 1990"),
    ("spector-supersymmetry-mobius", "Spector supersymmetry Moebius function zeta 1990"),
    ("bakas-bowick-arithmetic-gases", "Bakas Bowick curiosities of arithmetic gases 1991"),
    ("bost-connes-hecke", "Bost Connes Hecke algebras type III phase transitions number theory 1995"),
]

def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except Exception as e:
            if i == tries - 1:
                return {"_error": str(e)}
            time.sleep(2 + 2 * i)

def openalex(qstr):
    u = "https://api.openalex.org/works?search=" + urllib.parse.quote(qstr) + f"&mailto={MAIL}&per_page=5"
    d = get(u)
    return [{"title": w.get("title"), "year": w.get("publication_year"),
             "doi": w.get("doi"), "oa": (w.get("open_access") or {}).get("is_oa")}
            for w in d.get("results", [])]

def crossref(qstr):
    u = "https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(qstr) + f"&mailto={MAIL}&rows=5"
    d = get(u)
    return [{"title": (w.get("title") or [""])[0], "doi": w.get("DOI"),
             "container": (w.get("container-title") or [""])[0]}
            for w in d.get("message", {}).get("items", [])]

def arxiv(qstr):
    u = ("http://export.arxiv.org/api/query?search_query=all:" + urllib.parse.quote(qstr) +
         "&max_results=5")
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "QNFO/1.0"})
        x = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    except Exception as e:
        return [{"_error": str(e)}]
    return [{"title": t.strip(), "date": y[:10]}
            for t, y in re.findall(r"<title>([^<]+)</title>\s*<summary>[^<]*</summary>[^<]*<published>([^<]+)</published>", x)
            if t.strip().lower() not in ("arxiv api", "interdisciplinary physics")]

out = {}
for key, qstr in QUERIES:
    out[key] = {"query": qstr, "openalex": openalex(qstr),
                "crossref": crossref(qstr), "arxiv": arxiv(qstr)}
    time.sleep(0.4)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("saved", OUT)
for key, _ in QUERIES:
    v = out[key]
    oa = v["openalex"]; cr = v["crossref"]; ax = v["arxiv"]
    print(key, "| oa:", len(oa) if isinstance(oa, list) else oa,
          "| cr:", len(cr) if isinstance(cr, list) else cr,
          "| arx:", len(ax) if isinstance(ax, list) else ax)
    for h in (oa if isinstance(oa, list) else [])[:2]:
        print("   oa:", str(h.get("title"))[:70], h.get("year"), h.get("doi"))
    for h in (cr if isinstance(cr, list) else [])[:2]:
        print("   cr:", str(h.get("title"))[:70], h.get("doi"), h.get("container"))
