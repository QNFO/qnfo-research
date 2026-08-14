# Gateway JSON-LD Fix — Deployment Runbook (K-1)

**WBS:** QNFO.RES.008.P8-K1 (HARD finding F1 from post-publication audit)
**Status:** FIX COMMITTED — DEPLOYMENT BLOCKED (no canonical qnfo-gateway wrangler.toml in any local repo)
**Date:** 2026-08-14

## The Bug

papers.qnfo.org served INVALID ScholarlyArticle JSON-LD on **every paper page** (site-wide).
`json.loads` fails with "Extra data: line 1 column 2129": the JSON-LD block was not closed
with a real `</script>` — the source contained a double-escaped closer that JS rendered as
the literal string `<\/script>`, so the browser swallowed the JSON-LD block + `<title>` +
`<style>` + MathJax config until the next real `</script>`. Side effect: MathJax config never
executed (math may render with defaults).

**Root cause:** `QNFO/qwav-platform` → `qnfo-cloudflare-workers/qnfo-gateway.js` line 384:

```js
// BROKEN (double-escaped in source):
return '<script type="application/ld+json">' + jsonStr + "<\\/script>";
// JS evaluates "<\\/script>" to the literal string "<\/script>" (backslash preserved)
// → NOT a real closing tag → invalid JSON-LD block
```

**Fix (committed):** `fix/gateway-jsonld-closing-tag` branch, commit `64b9847`:

```js
// FIXED:
return '<script type="application/ld+json">' + jsonStr + "</script>";
```

The `\\u003c` / `\\u003e` / `\\u0026` JSON escaping on the preceding line is CORRECT
(valid JSON escapes) and was left unchanged. The other 10 single-escaped `<\/script>`
occurrences in `renderPaperHTML` are correct (JS renders them as real closers).

## Deployment Steps (for the next cycle / operator)

1. **Locate the canonical deploy config:** the deployed worker is `qnfo-gateway`
   (Cloudflare account edb167b78c9fb901ea5bca3ce58ccc4b). It serves
   `qnfo.org`, `papers.qnfo.org`, `legal.qnfo.org`, `graph-api.qnfo.org`
   (Tier-1 Gateway, 17 routes). The wrangler.toml for THIS worker was NOT found in
   `QNFO/qwav-platform` (only `qnfo-publications` Pages config exists) nor in
   `QNFO/infrastructure` (workers/qnfo-gateway/ has worker.js only). Find the config
   (deployment history, Cloudflare dashboard, or ask the deploying session) before
   deploying — it must carry routes + D1 bindings (LIVING_PAPER, QNFO_GRAPH) + any
   secrets. **Do NOT hand-build the config blindly** (route/binding mismatch would
   break the gateway).

2. **Checkout the fix:**
   ```
   git fetch origin fix/gateway-jsonld-closing-tag
   git checkout fix/gateway-jsonld-closing-tag
   ```

3. **Deploy with the canonical config** (example; adjust to the real config location):
   ```
   npx wrangler deploy qnfo-cloudflare-workers/qnfo-gateway.js
   # with CLOUDFLARE_API_TOKEN having Workers Scripts:Edit for qnfo-gateway
   ```

4. **Verify (mandatory):** `json.loads` on the ld+json block of 3+ paper pages:
   ```
   python -c "import requests,json,re; \
   for s in ['formal-self-reference-limits','prime-valuation-depth','universal-computational-topos']: \
     t=requests.get(f'https://papers.qnfo.org/papers/{s}').text; \
     b=re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',t,re.DOTALL); \
     print(s, 'VALID' if b and json.loads(b[0]) else 'INVALID')"
   ```
   All three must print VALID. Also confirm `window.MathJax` config executes (no longer
   swallowed) — check the page renders math with the configured inlineMath `$...$`.

5. **Same check for `qnfo-gateway-production`** (staging/prod variant, created 2026-07-31)
   before/after prod deploy if it serves the same template.

## Verification Evidence (pre-deploy)

- Reviewer subagent 8s4Rs5NK52mxnzCRV3s0F (P8 audit): HARD finding F1 with exact char offsets.
- Direct re-verification 2026-08-14: RES.008 / RES.005 / UCT pages all HTTP 200 but
  `JSONDecodeError: Extra data: line 1 column 2129 / 812 / 513` — identical broken structure.
- Fix branch confirmed on origin: raw fetch of `fix/gateway-jsonld-closing-tag` line 384
  shows `"</script>"` with 0 double-escapes remaining.

## Related Items

- K-2 (audit-the-auditor): P8 gate 6 must validate JSON-LD with `json.loads`, not string
  presence — applied in the P8 v1.1 audit and in this runbook's verify step.
- The Zenodo artifact itself was NEVER affected (deposit .md/.html/.pdf clean).
