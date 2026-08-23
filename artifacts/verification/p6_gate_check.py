#!/usr/bin/env python3
"""P6 DOI citation audit v2: DataCite (authoritative) + Zenodo search fallback.
Per DOIDOT-403-BOT-1: doi.org HEAD/GET = bot-blocked; authoritative = DataCite
state=findable (qnfo-audit UA) + Zenodo records search state=done/published."""
import json
import sys
import urllib.parse
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 qnfo-audit"}
OUT = sys.argv[1] if len(sys.argv) > 1 else "artifacts/verification/p6_gate_check.json"

def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())

dois = {
    "consilience_framework": "10.5281/zenodo.21804073",
    "atlas_F2": "10.5281/zenodo.21722395",
    "consilience_physics_numtheory": "10.5281/zenodo.21590155",
    "measurement_stratigraphy": "10.5281/zenodo.21705220",
    "valuation_without_r": "10.5281/zenodo.21803677",
    "tree_numeration": "10.5281/zenodo.21046213",
    "prime_valuation_depth": "10.5281/zenodo.21918838",
    "projective_geometric": "10.5281/zenodo.19564091",
}

results = {}
for key, doi in dois.items():
    entry = {"doi": doi}
    # 1) DataCite
    try:
        st, rec = get_json('https://api.datacite.org/dois/' + urllib.parse.quote(doi))
        attrs = rec.get("data", {}).get("attributes", {}) if st == 200 else {}
        entry["datacite"] = {"status": st, "state": attrs.get("state"),
                             "title": (attrs.get("titles") or [{}])[0].get("title")}
    except Exception as e:
        entry["datacite"] = {"error": str(e)}
    # 2) Zenodo search fallback
    try:
        st, rec = get_json('https://zenodo.org/api/records?q=' + urllib.parse.quote(f'doi:"{doi}"') + '&size=5')
        hits = rec.get("hits", {}).get("hits", []) if st == 200 else []
        entry["zenodo_search"] = {"status": st, "total": rec.get("hits", {}).get("total"),
                                  "hits": [{"id": h.get("id"), "state": h.get("status"),
                                            "title": h.get("metadata", {}).get("title")} for h in hits]}
    except Exception as e:
        entry["zenodo_search"] = {"error": str(e)}
    # verdict: DataCite findable OR Zenodo published
    dc_ok = entry.get("datacite", {}).get("state") == "findable"
    zs_ok = any(h.get("state") == "published" for h in entry.get("zenodo_search", {}).get("hits", []))
    entry["verdict"] = "OK" if (dc_ok or zs_ok) else "UNVERIFIED"
    results[key] = entry

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
