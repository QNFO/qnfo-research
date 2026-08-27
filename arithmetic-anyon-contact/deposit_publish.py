#!/usr/bin/env python3
"""QNFO.RES.028 — deposit_publish.py: metadata PUT + full source pack upload + publish.
Deposit 22124744 (concept 22124743). Token read from the local token file, never embedded."""
import json
import os
import sys
import time
import urllib.request

DEPOSIT_ID = 22124744
BASE = "https://zenodo.org/api/deposit/depositions"
TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 qnfo-audit")

ABSTRACT_PLAIN = (
    "Three spatial dimensions admit exactly two exchange statistics for identical "
    "particles, and a recent record reads the two occupation distributions as "
    "maximum-entropy occupations of one integer lattice under two multiplicity rules, "
    "closing with an open correspondence: the bounded-occupation family interpolates "
    "between the fermionic and bosonic cases and is proposed as the arithmetic object "
    "that intermediate (anyonic) statistics must contact. This paper settles the "
    "correspondence computationally. The family is the partition function of Gentile "
    "intermediate statistics - an occupation cap per mode - and it carries no exchange "
    "phase for any cap: permuting occupation labels yields only the signs +1 and -1, "
    "every observable is invariant under any inserted phase, and the canonical "
    "symmetric reading assigns the phase +1 for every cap, including the cap that "
    "reproduces Fermi counting, where fermions carry -1. The correspondence with Fermi "
    "counting is therefore a counting isomorphism, not an exchange-phase isomorphism. "
    "The arithmetic objects that carry the phases realized in the standard anyon "
    "models are multiplicative characters at roots of unity: the Laughlin exchange "
    "phase at filling 1/m is a primitive 2m-th root of unity, and the Fibonacci braid "
    "eigenvalues are powers of e^{i pi/5}. The prime-gap structure supplies a "
    "computable distinguishing observable: the specific heat of the primon gas "
    "deviates from the smooth-density-of-states ideal gas at every sampled "
    "temperature, by up to roughly three quarters at low temperature, in both "
    "statistics. The claims are isomorphisms of mathematical structure; the "
    "spin-statistics boundary is respected; every quantitative statement is "
    "reproduced by the deposited verification scripts.")

METADATA = {
    "title": ("Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, "
              "and the Roots of Unity That Carry Braid Phases"),
    "creators": [{"name": "Quni-Gudzinas, Rowan Brad",
                  "affiliation": "QNFO",
                  "orcid": "0009-0002-4317-5604"}],
    "description": ABSTRACT_PLAIN,
    "publication_date": "2026-08-27",
    "upload_type": "publication",
    "publication_type": "preprint",
    "license": "cc-by-4.0",
    "access_right": "open",
    "keywords": ["anyons", "Gentile statistics", "Haldane exclusion statistics",
                 "roots of unity", "Riemann gas", "Bose-Einstein statistics",
                 "Fermi-Dirac statistics", "bounded occupation", "zeta function"],
    "related_identifiers": [
        {"relation": "isSupplementTo",
         "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/arithmetic-anyon-contact"},
        {"relation": "cites", "identifier": "10.5281/zenodo.22123068"},
        {"relation": "cites", "identifier": "10.5281/zenodo.21208491"},
        {"relation": "cites", "identifier": "10.5281/zenodo.22024856"},
        {"relation": "cites", "identifier": "10.5281/zenodo.22035210"},
    ],
    "notes": ("Adjudicates the open correspondence of 10.5281/zenodo.22123068 "
              "(bounded-occupation family vs anyonic exchange phases): the family "
              "carries no exchange phase for any cap; the phase-carrying arithmetic "
              "objects are multiplicative characters at roots of unity. Verification "
              "suite deposited; all 22 citations verified live."),
}

FILES = [
    "arithmetic-anyon-contact.md",
    "arithmetic-anyon-contact.html",
    "arithmetic-anyon-contact.pdf",
    "references.bib",
    "citation-audit.md",
    "README.md",
    "PROJECT-PLAN.md",
    "LICENSE",
    "artifacts/universal-ignorance-audit.md",
    "artifacts/due-diligence-p1.md",
    "artifacts/consilience-gate.md",
    "artifacts/results-p4-reconciliation.md",
    "artifacts/external-search/arxiv-primon-gas-2026-08-27.json",
    "artifacts/external-search/arxiv-haldane-anyon-2026-08-27.json",
    "artifacts/external-search/citation-verify.json",
    "artifacts/verification/README.md",
    "artifacts/verification/verify_m_anyon.py",
    "artifacts/verification/verify_braid_characters.py",
    "artifacts/verification/verify_prime_gap_thermo.py",
    "artifacts/verification/verify_m_anyon.json",
    "artifacts/verification/verify_braid_characters.json",
    "artifacts/verification/verify_prime_gap_thermo.json",
    "artifacts/verification/final_m_anyon.log",
    "artifacts/verification/final_braid.log",
    "artifacts/verification/final_prime_gap.log",
    "check_rendering.py",
    "citation-verify.py",
    "render-pdf.cjs",
    "deposit_publish.py",
]


def request(method, url, body=None, headers=None, is_json=True):
    if body is None:
        data = None
    elif isinstance(body, (bytes, bytearray)):
        data = bytes(body)
    else:
        data = json.dumps(body).encode()
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    if body is not None and is_json and not isinstance(body, (bytes, bytearray)):
        h["Content-Type"] = "application/json"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=data, method=method, headers=h)
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                return (r.status, json.loads(raw) if raw and is_json else raw)
        except urllib.error.HTTPError as e:
            body_err = e.read().decode(errors="replace")[:300]
            if attempt == 3:
                return (e.code, body_err)
            print(f"  retry {attempt + 1} after {e.code}: {body_err}")
            time.sleep(3 + 3 * attempt)
        except Exception as e:
            if attempt == 3:
                return (0, str(e))
            print(f"  retry {attempt + 1} after transport error: {e}")
            time.sleep(3 + 3 * attempt)


# ---- 1. metadata PUT ----
print("PUT metadata ...")
status, resp = request("PUT", f"{BASE}/{DEPOSIT_ID}?access_token={TOKEN}",
                       {"metadata": METADATA})
print("metadata PUT:", status, str(resp)[:200])
if status != 200:
    sys.exit(1)

# ---- 2. uploads ----
ok_uploads = 0
for rel in FILES:
    path = rel.replace("/", os.sep)
    with open(path, "rb") as f:
        content = f.read()
    boundary = f"----qnfo{int(time.time() * 1000)}"
    parts = []
    parts.append(f"--{boundary}".encode())
    parts.append(f'Content-Disposition: form-data; name="name"'.encode())
    parts.append(b"")
    parts.append(rel.encode())
    parts.append(f"--{boundary}".encode())
    parts.append(f'Content-Disposition: form-data; name="file"; filename="{os.path.basename(path)}"'.encode())
    parts.append(b"Content-Type: application/octet-stream")
    parts.append(b"")
    parts.append(content)
    parts.append(f"--{boundary}--".encode())
    payload = b"\r\n".join(parts)
    status, resp = request("POST", f"{BASE}/{DEPOSIT_ID}/files?access_token={TOKEN}",
                           payload, headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
                           is_json=False)
    if status == 201:
        ok_uploads += 1
        print(f"  upload OK ({ok_uploads}/{len(FILES)}): {rel}")
    else:
        print(f"  upload FAIL {status}: {rel} :: {str(resp)[:200]}")
        sys.exit(1)

# ---- 3. publish ----
print("publish ...")
status, resp = request("POST", f"{BASE}/{DEPOSIT_ID}/actions/publish?access_token={TOKEN}")
print("publish:", status, str(resp)[:300])
if status != 202:
    sys.exit(1)
print("PUBLISHED 10.5281/zenodo.22124744")
