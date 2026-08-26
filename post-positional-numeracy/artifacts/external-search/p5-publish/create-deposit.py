# -*- coding: utf-8 -*-
"""create-deposit.py — QNFO.RES.024: create Zenodo deposit + reserve DOI (2026-08-26).

Deposit API shape (ZENODO-DEPOSIT-CREATE-SHAPE-1: wrapped {"metadata": {...}});
DOI reservation via records API POST /api/records/{id}/draft/pids/doi
(PRERESERVE-VIA-RECORDS-API-RESERVE_DOI-1). Evidence saved to this directory.
"""
import json, os, sys, urllib.request

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

def req(method, path, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    r = urllib.request.Request(BASE + path, data=data, method=method, headers={
        "User-Agent": UA, "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": BASE + "/", "Origin": BASE,
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(r, timeout=60) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

ABSTRACT = (
    "Exact computation on the rationals today inhabits a single completion. Digital arithmetic runs "
    "in the real numbers and accepts rounding; exact alternatives run in a single p-adic completion "
    "through Hensel codes and reconstruct through the Chinese remainder theorem with Farey bounds. "
    "This paper develops the multi-place realization that joins the two. A rational number is encoded "
    "by its residues at finitely many chosen primes together with a two-sided Archimedean window; the "
    "encoding is injective whenever 2 B^2 < M, where M is the product of the chosen prime powers. The "
    "adelic product formula - the identity that ties the places of the rationals together - becomes a "
    "machine-checkable invariant of the arithmetic: every correct encode-compute-decode round-trip of "
    "operands whose numerator and denominator factor over the chosen primes satisfies it exactly, and "
    "any violation localizes the failing place. All claims are computationally verified: golden values, "
    "exhaustive injectivity on small moduli, 100000 seeded trials on a window of modulus M = 810000, "
    "80000 componentwise arithmetic checks, and a reconstruction algorithm validated against exhaustive "
    "enumeration. A dependency-free reference implementation and a reproducibility statement accompany "
    "the paper."
)

metadata = {
    "title": "Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic",
    "upload_type": "publication",
    "publication_type": "preprint",
    "publication_date": "2026-08-26",
    "description": ABSTRACT,
    "access_right": "open",
    "license": "CC-BY-4.0",
    "creators": [{"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO"}],
    "keywords": [
        "finite adeles", "Hensel codes", "product formula", "exact rational arithmetic",
        "Ostrowski's theorem", "rational reconstruction", "non-Archimedean", "numeration",
    ],
    "related_identifiers": [
        {"scheme": "url", "relation": "isSupplementTo",
         "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/post-positional-numeracy"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.20756222"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.21148596"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.1016/j.jsc.2025.102481"},
    ],
    "version": "1.0.0",
}

def save(name, obj):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)

st, d = req("POST", "/api/deposit/depositions", {"metadata": metadata})
save("deposit-create.json", {"status": st, "body": d})
print("CREATE", st, "deposit_id:", d.get("id"), "conceptrecid:", d.get("conceptrecid"))
if st not in (200, 201):
    print("ERROR BODY:", json.dumps(d)[:800])
    sys.exit(1)

dep = d["id"]
st2, d2 = req("POST", "/api/records/%s/draft/pids/doi" % dep)
save("deposit-reserve-doi.json", {"status": st2, "body": d2})
print("RESERVE-DOI", st2, "doi:", d2.get("doi") if isinstance(d2, dict) else d2)
