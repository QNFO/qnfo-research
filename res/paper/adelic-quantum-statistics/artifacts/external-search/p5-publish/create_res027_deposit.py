# -*- coding: utf-8 -*-
"""create_res027_deposit.py — QNFO.RES.027 P8: create Zenodo deposit + reserve DOI (2026-08-27).

Pattern per ZENODO-DEPOSIT-CREATE-SHAPE-1 (wrapped {"metadata": {...}}) and
PRERESERVE-VIA-RECORDS-API-RESERVE_DOI-1 (records API POST /api/records/{id}/draft/pids/doi).
Evidence saved to this directory.
"""
import json, os, sys, time, urllib.request, urllib.error

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

def req(method, path, body=None, tries=6):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(BASE + path, data=data, method=method, headers={
                "User-Agent": UA, "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": BASE + "/", "Origin": BASE,
                "Authorization": "Bearer " + TOKEN,
                "Content-Type": "application/json",
            })
            with urllib.request.urlopen(r, timeout=60) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                last = (e.code, json.loads(e.read().decode("utf-8")))
            except Exception:
                last = (e.code, str(e))
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            return e.code, last[1]
        except Exception as e:
            last = ("NET", str(e))
            time.sleep(3 + 4 * i)
    return (0, last)

ABSTRACT = (
    "Why are there two quantum statistics, and only two, in three spatial dimensions? This paper "
    "reads the Bose-Einstein and Fermi-Dirac occupation distributions as the maximum-entropy "
    "solutions of one lattice with two multiplicity rules. On the unrestricted integer lattice the "
    "Euler factor at each prime place is the mode partition function of an unbounded occupation "
    "number, and the resulting Dirichlet series is the Riemann zeta function; on the squarefree "
    "restriction - each prime divides at most once - the Euler factor becomes the mode partition "
    "function of an occupation number in {0,1}, and the series becomes a ratio of two zeta values. "
    "The two golden occupation numbers follow from the canonical derivative of these mode factors "
    "at arbitrary inverse temperature and chemical potential, and both are the unique "
    "maximum-entropy distributions under their stated constraints. The per-place identifications at "
    "fugacity z = 1/p were established elsewhere; what the earlier records leave open is supplied "
    "here: the per-distinction transition rate gamma = 1/N as a consequence of bath degeneracy, the "
    "complex structure of the large-N limit as the sign-normalized generator selected by exclusion, "
    "the Moebius-parity reading of composite statistics, and the bounded-occupation family that "
    "interpolates between the two statistics and that anyonic exchange statistics must contact. The "
    "register is structural throughout: no physical particle is implied; the claims are isomorphisms "
    "of mathematical structure, and the physical labels attach at the level of statistical "
    "distributions. Every quantitative statement is reproduced by the deposited verification scripts."
)

metadata = {
    "title": "Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi-Dirac/Bose-Einstein Distinction",
    "upload_type": "publication",
    "publication_type": "preprint",
    "publication_date": "2026-08-27",
    "description": ABSTRACT,
    "access_right": "open",
    "license": "CC-BY-4.0",
    "creators": [{"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO"}],
    "keywords": [
        "Bose-Einstein statistics", "Fermi-Dirac statistics", "squarefree integers",
        "adelic product formula", "maximum entropy", "Mobius function", "anyons",
        "bounded occupation", "primon gas", "quantum statistics",
    ],
    "related_identifiers": [
        {"scheme": "url", "relation": "isSupplementTo",
         "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/adelic-quantum-statistics"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.22035210"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.22046458"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.22117282"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.22024240"},
    ],
    "version": "1.0.0",
}

def save(name, obj):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)

st, d = req("POST", "/api/deposit/depositions", {"metadata": metadata})
save("deposit-create.json", {"status": st, "body": d})
print("CREATE", st, "deposit_id:", d.get("id") if isinstance(d, dict) else "?", "conceptrecid:", d.get("conceptrecid") if isinstance(d, dict) else "?")
if st not in (200, 201):
    print("ERROR BODY:", json.dumps(d)[:600])
    sys.exit(1)

dep = d["id"]
st2, d2 = req("POST", "/api/records/%s/draft/pids/doi" % dep)
save("deposit-reserve-doi.json", {"status": st2, "body": d2})
doi = d2.get("doi") if isinstance(d2, dict) else None
print("RESERVE-DOI", st2, "doi:", doi)

summary = {"deposit_id": dep, "conceptrecid": d.get("conceptrecid"), "reserved_doi": doi,
           "concept_doi": ("10.5281/zenodo.%s" % d["conceptrecid"]) if d.get("conceptrecid") else None,
           "record_doi": doi}
save("deposit-summary.json", summary)
print("SUMMARY", json.dumps(summary))
