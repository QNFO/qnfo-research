# -*- coding: utf-8 -*-
"""p7_send.py — QNFO.RES.027 P7 outreach: key, institutional checks, test-send, first contacts."""
import json, os, re, time, urllib.request, urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
CF_ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
HERE = os.path.dirname(os.path.abspath(__file__))
DOI = "10.5281/zenodo.22123068"
SEND = "https://qnfo-email.q08.workers.dev/send"

def get(url, headers=None, tries=5):
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(r, timeout=60) as resp:
                return resp.status, resp.read()
        except Exception:
            time.sleep(3 + 4 * i)
    return (0, b"")

# 1. key from /bindings (API_KEY is plain_text)
st, body = get("https://api.cloudflare.com/client/v4/accounts/%s/workers/scripts/qnfo-email/bindings" % CF_ACCT,
               {"Authorization": "Bearer " + CF_TOKEN, "Content-Type": "application/json"})
key = None
if st == 200:
    j = json.loads(body.decode())
    for b in j.get("result", []):
        if b.get("name") == "API_KEY" and b.get("text"):
            key = b["text"]
print("KEY-FROM-BINDINGS", st, "key:", bool(key), "tail:", key[-14:] if key else None)

# 2. institutional checks (Hartnoll Stanford, Hazzard Rice) — page text grep
def page_emails(url):
    st, b = get(url, {"User-Agent": UA})
    if st != 200:
        return set(), st
    txt = b.decode("utf-8", "replace")
    return set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", txt)), st

for name, url in (
    ("Hartnoll-Stanford", "https://physics.stanford.edu/people/sean-hartnoll"),
    ("Hazzard-Rice", "https://hazzard.rice.edu/"),
):
    emails, st = page_emails(url)
    hits = sorted(e.lower() for e in emails if "hartnoll" in e.lower() or "hazzard" in e.lower())
    print("INST", name, st, hits[:4])

if not key:
    print("NO KEY — ABORT SENDS")
    raise SystemExit(0)

auth = {"Authorization": "Bearer " + key, "User-Agent": UA, "Content-Type": "application/json"}

def send(to, subject, body_text):
    payload = {"to": to, "subject": subject, "body": body_text, "from": "rowan@qnfo.org"}
    data = json.dumps(payload).encode("utf-8")
    st, b = get(SEND, dict(auth), tries=5)
    r2 = urllib.request.Request(SEND, data=data, method="POST", headers=auth)
    try:
        with urllib.request.urlopen(r2, timeout=60) as resp:
            st2 = resp.status
            b2 = resp.read()
    except urllib.error.HTTPError as e:
        st2 = e.code
        b2 = e.read()
    return st2, b2[:200]

# 3. test-send to own mailbox (TEST-SEND-EXTERNAL-1)
st_t, b_t = send("rwnquni@outlook.com",
                 "Pre-publish check: QNFO squarefree-statistics preprint",
                 "Internal delivery check for the RES.027 outreach batch. Record: %s" % DOI)
print("TEST-SEND", st_t, b_t)

# 4. first contacts (one per group, source-verified)
contacts = [
    ("nicolas.medina.sanchez@univie.ac.at",
     "The squarefree origin of the Bose-Fermi dichotomy",
     "Dear Dr Medina Sanchez,\n\nA new preprint from QNFO derives the Bose-Einstein and Fermi-Dirac "
     "occupation distributions as the maximum-entropy solutions of one integer lattice under two "
     "multiplicity rules, with the bounded-occupation family interpolating between them: "
     "%s (10.5281/zenodo.22123068). Your reconstruction program for particle statistics is the closest "
     "operational counterpart, and the interpolation family there is proposed as the arithmetic object "
     "the reconstructed statistics should contact. With kind regards,\nRowan Brad Quni-Gudzinas, QNFO" % DOI),
    ("daiwusheng@tju.edu.cn",
     "The squarefree origin of the Bose-Fermi dichotomy",
     "Dear Professor Dai,\n\nA new preprint from QNFO reads the Bose-Einstein and Fermi-Dirac occupation "
     "distributions as the maximum-entropy solutions of one integer lattice under two multiplicity rules, "
     "with the bounded-occupation family interpolating between them: %s (10.5281/zenodo.22123068). Your "
     "result that quantum statistics forbids exchange statistics beyond bosons and fermions in three "
     "dimensions is the natural three-dimensional boundary for that family. With kind regards,\n"
     "Rowan Brad Quni-Gudzinas, QNFO" % DOI),
]
results = []
for to, subj, body in contacts:
    st_s, b_s = send(to, subj, body)
    results.append({"to": to, "status": st_s, "resp": b_s.decode("utf-8", "replace")})
    print("SEND", to, st_s, b_s.decode("utf-8", "replace")[:150])

json.dump(results, open(os.path.join(HERE, "p7-send-results.json"), "w"), indent=1)
print("P7 SENDS DONE")
