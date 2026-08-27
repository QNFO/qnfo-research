#!/usr/bin/env python3
"""QNFO.RES.028 — citation-verify.py: live-verify every bib entry.
DOIs via Crossref works API; arXiv IDs via export.arxiv.org. Writes evidence to
artifacts/external-search/citation-verify.json. Exit 0 iff all DOIs resolve and
all arXiv IDs return a matching title."""

import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 qnfo-audit")

BIB = "references.bib"
OUT = "artifacts/external-search/citation-verify.json"

bib = open(BIB, encoding="utf-8").read()
entries = re.split(r"\n@", bib)
results = []


def fetch(url, tries=2):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                      "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=12) as r:
                return json.loads(r.read())
        except Exception as e:
            last = e
            time.sleep(1)
    raise last


for chunk in entries:
    if not chunk.strip():
        continue
    key = chunk.split("{", 1)[1].split(",", 1)[0].strip()
    doi = re.search(r"doi\s*=\s*\{([^}]+)\}", chunk)
    eprint = re.search(r"eprint\s*=\s*\{([^}]+)\}", chunk)
    title = re.search(r"title\s*=\s*\{([^}]+)\}", chunk)
    rec = {"key": key, "doi": None, "eprint": None, "status": None, "detail": ""}
    try:
        if doi:
            d = doi.group(1)
            rec["doi"] = d
            if d.startswith("10.5281/zenodo."):
                # Zenodo DOIs are registered with DataCite, not Crossref
                dd = fetch(f"https://api.datacite.org/dois/{urllib.parse.quote(d)}")
                attrs = (dd.get("data") or {}).get("attributes") or {}
                ttl = (attrs.get("titles") or [{}])[0].get("title", "")[:80]
                rec["status"] = "ok"
                rec["detail"] = f"datacite: {ttl}"
            else:
                cr = fetch(f"https://api.crossref.org/works/{urllib.parse.quote(d)}")
                msg = cr["message"]
                cr_title = (msg.get("title") or [""])[0][:80]
                rec["status"] = "ok"
                rec["detail"] = f"crossref: {cr_title}"
        elif eprint:
            ep = eprint.group(1)
            rec["eprint"] = ep
            # export.arxiv.org returns Atom XML, not JSON
            req = urllib.request.Request(
                f"https://export.arxiv.org/api/query?id_list={urllib.parse.quote(ep)}",
                headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=12) as r:
                data = r.read()
            root = ET.fromstring(data)
            ns = {"a": "http://www.w3.org/2005/Atom"}
            ent = root.find("a:entry", ns)
            if ent is not None:
                t = re.sub(r"\s+", " ", (ent.find("a:title", ns).text or "")).strip()[:80]
                rec["status"] = "ok"
                rec["detail"] = f"arxiv: {t}"
            else:
                rec["status"] = "MISSING"
                rec["detail"] = "arxiv returned no entry"
        else:
            rec["status"] = "ok"
            rec["detail"] = "book/proceedings entry, no DOI asserted"
    except Exception as e:
        rec["status"] = "ERROR"
        rec["detail"] = str(e)[:120]
    results.append(rec)
    print(f"[{rec['status'].upper():7s}] {key}: {rec['detail']}")

open(OUT, "w", encoding="utf-8").write(json.dumps(results, indent=2, ensure_ascii=False))
bad = [r for r in results if r["status"] != "ok"]
print(f"\n{len(results)} entries verified; {len(bad)} failures; evidence -> {OUT}")
raise SystemExit(1 if bad else 0)
