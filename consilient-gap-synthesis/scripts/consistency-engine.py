#!/usr/bin/env python3
"""Consistency Engine v0.1 — Cross-Ecosystem Verification (OI-003 / I-01)

Queries D1 for paper metadata consistency and spot-checks papers-server health.
Run: python scripts/consistency-engine.py

Checks:
  1. Paper count vs paper_ids delta
  2. NULL/PENDING DOI coverage
  3. Published paper HTTP health (sample)
"""

import urllib.request, json, os, sys
from datetime import datetime

CLOUDFLARE_TOKEN = os.environ.get('CLOUDFLARE_API_TOKEN', '')
ACCOUNT_ID = 'edb167b78c9fb901ea5bca3ce58ccc4b'
LIVING_PAPER_DB = '70a58cb3-b2cd-498d-877f-ecca86859a22'
HEADERS = {'Authorization': f'Bearer {CLOUDFLARE_TOKEN}', 'Content-Type': 'application/json'}

def d1(sql, params=None):
    body = json.dumps({'sql': sql, 'params': params or []})
    req = urllib.request.Request(
        f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/d1/database/{LIVING_PAPER_DB}/query',
        data=body.encode(), headers=HEADERS)
    return json.loads(urllib.request.urlopen(req).read())

if __name__ == '__main__':
    if not CLOUDFLARE_TOKEN:
        print("ERROR: CLOUDFLARE_API_TOKEN not set"); sys.exit(1)
    
    print(f"=== QNFO Consistency Engine v0.1 ===\n{datetime.utcnow().isoformat()}Z\n")
    
    issues = []
    
    # 1. Paper Count
    total = d1("SELECT COUNT(*) as c FROM papers")['result'][0]['results'][0]['c']
    pids = d1("SELECT COUNT(*) as c FROM paper_ids")['result'][0]['results'][0]['c']
    body = d1("SELECT COUNT(*) as c FROM papers WHERE body_md IS NOT NULL AND body_md != ''")['result'][0]['results'][0]['c']
    delta = total - pids
    print(f"Papers: {total} | paper_ids: {pids} | body: {body} | delta: {delta}")
    if delta > 0:
        issues.append(f"PAPER-IDS-GAP: {delta} papers missing ({total} total, {pids} registered)")
    
    # 2. DOI Coverage
    null = d1("SELECT COUNT(*) as c FROM papers WHERE doi IS NULL OR doi IN ('','NULL','PENDING') OR doi LIKE 'PENDING%'")['result'][0]['results'][0]['c']
    print(f"NULL-DOIs: {null}")
    if null > 0:
        issues.append(f"NULL-DOI: {null} papers without DOI")
    
    # 3. Published Paper Health (sample 10)
    pubs = d1("SELECT slug FROM papers WHERE status='published' AND body_md IS NOT NULL AND body_md != '' LIMIT 10")['result'][0]['results']
    for p in pubs:
        try:
            req = urllib.request.Request(f'https://papers.qnfo.org/papers/{p["slug"]}/', method='HEAD')
            code = urllib.request.urlopen(req, timeout=10).getcode()
            if code != 200:
                issues.append(f"HTTP-{code}: {p['slug']}")
        except Exception as e:
            issues.append(f"ERROR: {p['slug']} — {type(e).__name__}")
    print(f"Spot-checked {len(pubs)} published papers")
    
    print(f"\n{'✅ ALL CLEAR' if not issues else f'⚠️  {len(issues)} ISSUE(S):'}")
    for i in issues: print(f"  {i}")
    sys.exit(len(issues))
