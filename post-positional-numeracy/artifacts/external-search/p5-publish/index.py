# -*- coding: utf-8 -*-
"""index.py — QNFO.RES.024: Vectorize index trigger + verify via direct connection (2026-08-26)."""
import json, sys, time, urllib.error, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
TOKEN = "chnx-idx-v1-k9m2n4p7r5t8"
HOST = "https://qnfo-paper-indexer.q08.workers.dev"

def call(method, url, tries=6):
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, method=method, headers={
                "User-Agent": UA, "Accept": "application/json",
                "X-Index-Token": TOKEN,
            })
            with urllib.request.urlopen(r, timeout=90) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                return e.code, json.loads(e.read().decode("utf-8"))
            except Exception:
                return e.code, {"__raw__": "http error body unreadable"}
        except Exception as e:
            last = e
            time.sleep(3 * (i + 1))
    return -1, {"__error__": str(last)}

st1, b1 = call("POST", HOST + "/webhook?slug=post-positional-numeracy")
print("TRIGGER", st1, json.dumps(b1)[:300])
time.sleep(5)
st2, b2 = call("GET", HOST + "/webhook?slug=post-positional-numeracy")
print("VERIFY", st2, json.dumps(b2)[:300])

ok = (st1 == 200) and (st2 == 200) and isinstance(b2, dict) and b2.get("indexed") is True
print("INDEXED:", ok)
sys.exit(0 if ok else 1)
