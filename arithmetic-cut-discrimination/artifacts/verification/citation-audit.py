# QNFO.RES.030 P5 citation audit — verify every reference is findable and correct.
# Crossref for journal DOIs, DataCite for Zenodo DOIs, arXiv API for eprints.
# Output: artifacts/verification/citation-audit-output.json + stdout summary.
import json, os, sys, time, urllib.request, urllib.parse

def fetch(url, timeout=25, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "QNFO-citation-audit/1.0 (mailto:rowan.quni@outlook.com)"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2 + 2 * i)
    return "ERROR:" + str(last)

ver_dir = os.path.dirname(os.path.abspath(__file__))
out = {"checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "refs": {}}

# --- arXiv eprint metadata (authors are authoritative from the API) ---
ids = "2411.15377,1401.8190,2502.02661"
raw = fetch("http://export.arxiv.org/api/query?id_list=" + ids + "&max_results=5")
import xml.etree.ElementTree as ET
ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
for entry in ET.fromstring(raw).findall("a:entry", ns):
    eid = entry.find("a:id", ns).text.split("/abs/")[-1]
    title = " ".join(entry.find("a:title", ns).text.split())
    authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
    out["refs"][eid] = {"kind": "arxiv", "status": "found",
                        "title": title, "authors": authors}
    print("ARXIV %s: %s | %s" % (eid, title[:60], "; ".join(authors)))

# --- Crossref journal DOIs ---
crossref = {
    "10.1007/978-3-642-75405-0_30": "julia1990statistical",
    "10.1051/jphys:0198900500120137100": "julia1989thermodynamic",
    "10.1063/1.529511": "bakas1991curiosities",
    "10.1016/0375-9601(89)90626-9": "spector1990supersymmetry",
    "10.1090/pspum/024/0337821": "montgomery1973pair",
    "10.1090/S0025-5718-1987-0866115-0": "odlyzko1987distribution",
    "10.1112/S0025579300011090": "gallagher1985distribution",
    "10.1098/rspa.1985.0078": "berry1985semiclassical",
    "10.1103/PhysRevLett.77.1472": "bogomolny1996gutzwiller",
    "10.1007/BF01553491": "bost1995hecke",
    "10.1063/1.1703773": "dyson1962statistical",
}
for doi, key in crossref.items():
    raw = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if raw.startswith("ERROR"):
        out["refs"][key] = {"kind": "crossref", "status": "error", "doi": doi, "detail": raw[:120]}
        print("CROSSREF %-36s ERROR %s" % (key, raw[:60]))
        continue
    try:
        j = json.loads(raw)
        t = j["message"].get("title", [""])
        out["refs"][key] = {"kind": "crossref", "status": "found", "doi": doi,
                            "title": t[0] if t else ""}
        print("CROSSREF %-36s FOUND  %s" % (key, (t[0] if t else "?")[:60]))
    except Exception as e:
        out["refs"][key] = {"kind": "crossref", "status": "parse-error", "doi": doi, "detail": str(e)}
        print("CROSSREF %-36s PARSE-ERROR %s" % (key, str(e)[:60]))

# --- DataCite Zenodo DOIs ---
zenodo = {
    "10.5281/zenodo.22150472": "quni2026ump014",
    "10.5281/zenodo.22133122": "quni2026stats",
    "10.5281/zenodo.22124744": "quni2026anyons",
    "10.5281/zenodo.22142794": "quni2026adelic",
    "10.5281/zenodo.22076816": "quni2026program",
}
for doi, key in zenodo.items():
    raw = fetch("https://api.datacite.org/dois/" + urllib.parse.quote(doi))
    if raw.startswith("ERROR"):
        out["refs"][key] = {"kind": "datacite", "status": "error", "doi": doi, "detail": raw[:120]}
        print("DATACITE %-36s ERROR %s" % (key, raw[:60]))
        continue
    try:
        j = json.loads(raw)
        d = j["data"]["attributes"]
        out["refs"][key] = {"kind": "datacite", "status": "found", "doi": doi,
                            "title": d.get("titles", [{}])[0].get("title", "")}
        print("DATACITE %-36s FOUND  %s" % (key, d.get("titles", [{}])[0].get("title", "?")[:60]))
    except Exception as e:
        out["refs"][key] = {"kind": "datacite", "status": "parse-error", "doi": doi, "detail": str(e)}
        print("DATACITE %-36s PARSE-ERROR %s" % (key, str(e)[:60]))

with open(os.path.join(ver_dir, "citation-audit-output.json"), "w") as f:
    json.dump(out, f, indent=1)
print("AUDIT DONE refs=%d" % len(out["refs"]))
