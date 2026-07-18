"""Verify Cloudflare tokens v2 - fixed error handling."""
import os, json, requests

ZONE_ID = "d6d1e08f7e9405a9cfa3d8f4630c9b0c"
ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"

# Read file token
token_path = os.path.join(os.environ["USERPROFILE"], ".cloudflare", "api-token-readonly")
file_token = ""
try:
    with open(token_path) as f:
        file_token = f.read().strip()
except:
    print(f"Cannot read {token_path}")

env_token = os.environ.get("CLOUDFLARE_API_TOKEN", "")

tokens = [
    ("env_var", env_token),
    ("file_readonly", file_token),
]

for name, token in tokens:
    if not token:
        print(f"\n{name}: EMPTY")
        continue

    print(f"\n=== {name} === (prefix: {token[:12]}...)")

    # Verify
    r = requests.get(
        "https://api.cloudflare.com/client/v4/user/tokens/verify",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    data = r.json()
    if data.get("success"):
        result = data.get("result", {})
        print(f"  VERIFY: OK | status={result.get('status')}")
        for pol in result.get("policies", []):
            for pg in pol.get("permission_groups", []):
                print(f"    perm: {pg.get('name','?')}")
    else:
        errors = data.get("errors", [])
        print(f"  VERIFY: FAIL | {errors[0].get('message','?')[:100] if errors else '?'}")

    # DNS test
    r = requests.get(
        f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records?per_page=1",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    d = r.json()
    print(f"  DNS read: {'OK' if d.get('success') else 'FAIL: '+str(d.get('errors',[{'message':'?'}])[0].get('message',''))}")

    # R2 test - list buckets
    try:
        r = requests.get(
            f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/r2/buckets",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        rd = r.json()
        if rd.get("success") and isinstance(rd.get("result"), list):
            names = [b.get("name","?") for b in rd["result"] if isinstance(b, dict)]
            print(f"  R2 buckets: OK - {names}")
        else:
            print(f"  R2 buckets: FAIL - {rd.get('errors',[{'message':'?'}])[0].get('message','')}")
    except Exception as e:
        print(f"  R2 buckets: ERROR - {e}")

    # DNS write test - try to create a TXT record
    test_name = f"_dnslink.test-{os.urandom(4).hex()}"
    r = requests.post(
        f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={"type": "TXT", "name": test_name, "content": "dnslink=/ipfs/test", "ttl": 60},
        timeout=10,
    )
    dw = r.json()
    if dw.get("success"):
        rec_id = dw["result"]["id"]
        print(f"  DNS write: OK (created {test_name}, id={rec_id})")
        # Clean up test record
        requests.delete(
            f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{rec_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )
        print(f"  DNS cleanup: OK")
    else:
        err = dw.get("errors", [{}])[0].get("message", "?")
        print(f"  DNS write: FAIL - {err[:150]}")

print("\nDone.")
