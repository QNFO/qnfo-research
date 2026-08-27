# -*- coding: utf-8 -*-
"""indexer_drain.py — poll the qnfo-paper-indexer to completion for the RES.027 slug."""
import json, time, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
IDX_TOKEN = "chnx-idx-v1-k9m2n4p7r5t8"
SLUG = "adelic-quantum-statistics"
OUT = r"C:\Users\LENOVO\Projects\qnfo-research\res\paper\adelic-quantum-statistics\artifacts\external-search\p5-publish\indexer-drain-report.txt"

lines = []
for call in range(20):
    try:
        r = urllib.request.Request(
            "https://qnfo-paper-indexer.q08.workers.dev/index?slug=%s" % SLUG,
            headers={"User-Agent": UA, "X-Index-Token": IDX_TOKEN})
        with urllib.request.urlopen(r, timeout=240) as resp:
            j = json.loads(resp.read().decode())
        line = ("call %d done=%s total=%s offset=%s pct=%s batch=%s" % (
            call, j.get("done"), j.get("total"), j.get("offset"), j.get("pct"),
            json.dumps(j.get("batch"))[:160]))
        print(line)
        lines.append(line)
        if j.get("done"):
            break
        time.sleep(4)
    except Exception as e:
        line = "call %d err %s" % (call, str(e)[:120])
        print(line)
        lines.append(line)
        time.sleep(10)

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("DRAIN-DONE", j.get("done") if 'j' in dir() else "unknown")
