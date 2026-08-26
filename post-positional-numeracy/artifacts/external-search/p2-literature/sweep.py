# -*- coding: utf-8 -*-
"""P2 literature sweep — QNFO.RES.024 post-positional-numeracy (2026-08-26).

OpenAlex + Crossref, keyless polite pool. Evidence output: p2-literature-sweep.json
Key targets: Ostrowski 1916/1918 (Acta Math), Wang-Guy-Davenport 1981 (SIGSAM),
Dixon 1982 (Numer. Math.), Krishnamurthy-Gregory error-free computation,
Krishnamurthy-Rao-Subramanian 1975 (Hensel codes), Boehm-Decker-Fieker-Pfister
(bad primes), Hensel p-adic numbers.
"""
import json, time, urllib.request, urllib.parse, os

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 (mailto: rwnquni@outlook.com)")

def get(url, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if i == tries - 1:
                return {"__error__": "%s: %s" % (type(e).__name__, e)}
            time.sleep(2 * (i + 1))

def slim_openalex(d):
    out = {"count": (d.get("meta") or {}).get("count"), "results": []}
    for w in (d.get("results") or []):
        auths = [a.get("author", {}).get("display_name") for a in (w.get("authorships") or [])]
        src = (w.get("primary_location") or {}).get("source") or {}
        out["results"].append({
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "doi": w.get("doi"),
            "authors": auths,
            "venue": src.get("display_name"),
        })
    return out

def slim_crossref(d):
    items = (d.get("message") or {}).get("items")
    if items is None:
        m = d.get("message") or {}
        if m.get("title"):
            return {"doi": m.get("DOI"), "title": m.get("title"),
                    "year": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0],
                    "authors": ["%s, %s" % (a.get("family"), a.get("given")) for a in (m.get("author") or [])],
                    "container": (m.get("container-title") or [None])[0],
                    "volume": m.get("volume"), "issue": m.get("issue"), "page": m.get("page")}
        return {"items": []}
    out = {"count": (d.get("message") or {}).get("total-results"), "results": []}
    for w in items:
        out["results"].append({
            "title": (w.get("title") or [None])[0],
            "year": ((w.get("issued") or {}).get("date-parts") or [[None]])[0][0],
            "doi": w.get("DOI"),
            "authors": ["%s, %s" % (a.get("family"), a.get("given")) for a in (w.get("author") or [])],
            "container": (w.get("container-title") or [None])[0],
            "volume": w.get("volume"), "issue": w.get("issue"), "page": w.get("page"),
        })
    return out

queries = [
    ("openalex", "https://api.openalex.org/works?filter=title.search:hensel%20codes&per-page=10&mailto=rwnquni@outlook.com"),
    ("openalex", "https://api.openalex.org/works?filter=title.search:p-adic%20reconstruction&per-page=10&mailto=rwnquni@outlook.com"),
    ("openalex", "https://api.openalex.org/works?search=error-free%20computation%20Krishnamurthy%20Gregory&per-page=10&mailto=rwnquni@outlook.com"),
    ("crossref-doi", "https://api.crossref.org/works/10.1007/BF02422942"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=Ostrowski+Funktionalgleichung+Acta+Mathematica+absolute+values&rows=5&mailto=rwnquni@outlook.com"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=p-adic+reconstruction+of+rational+numbers+Wang+Davenport&rows=5&mailto=rwnquni@outlook.com"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=exact+solution+of+linear+equations+using+p-adic+expansions+Dixon&rows=5&mailto=rwnquni@outlook.com"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=use+of+bad+primes+in+rational+reconstruction+Boehm&rows=5&mailto=rwnquni@outlook.com"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=Methods+and+Applications+of+Error-Free+Computation+Krishnamurthy&rows=5&mailto=rwnquni@outlook.com"),
    ("crossref", "https://api.crossref.org/works?query.bibliographic=Finite-segment+p-adic+number+systems+exact+computation&rows=5&mailto=rwnquni@outlook.com"),
]

out = {}
for name, url in queries:
    d = get(url)
    if name.startswith("openalex"):
        out[url] = slim_openalex(d)
    else:
        out[url] = slim_crossref(d)
    time.sleep(0.6)

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "p2-literature-sweep.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("WROTE p2-literature-sweep.json keys:", len(out))
