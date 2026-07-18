"""Verify Cloudflare tokens and test DNS + R2 capabilities."""
import os, json, requests, sys

# Token sources
env_token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
file_token = ""
token_path = os.path.join(os.environ["USERPROFILE"], ".cloudflare", "api-token-readonly")
try:
    with open(token_path) as f:
        file_token = f.read().strip()
except:
    pass

tokens = {
    "env_var": env_token,
    "readonly_file": file_token,
}

ZONE_ID = "d6d1e08f7e9405a9cfa3d8f4630c9b0c"

for name, token in tokens.items():
    if not token:
        print(f"{name}: EMPTY")
        continue

    print(f"\n=== {name} === ({token[:8]}...{token[-4:]})")

    # Verify token
    r = requests.get(
        "https://api.cloudflare.com/client/v4/user/tokens/verify",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    data = r.json()
    success = data.get("success", False)
    if success:
        result = data.get("result", {})
        print(f"  VERIFY: OK | status={result.get('status')}")
        pols = result.get("policies", [])
        for pol in pols:
            for pg in pol.get("permission_groups", []):
                print(f"    perm: {pg.get('name','?')}")
            for rg in pol.get("resource_groups", []):
                for scope in rg.get("scope", {}).get("zones", []):
                    print(f"    zone scope: {scope.get('name','?')} (id={scope.get('id','?')})")
    else:
        errors = data.get("errors", [])
        print(f"  VERIFY: FAIL | {errors}")

    # Test DNS list
    r2 = requests.get(
        f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records?per_page=1",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    dns_data = r2.json()
    print(f"  DNS read: {'OK' if dns_data.get('success') else 'FAIL ' + str(dns_data.get('errors',[]))}")

    # Test R2 write (via S3-compatible API)
    # Cloudflare R2 S3 endpoint: https://<account-id>.r2.cloudflarestorage.com
    # Let's check the Workers KV/R2 API instead
    r3 = requests.get(
        "https://api.cloudflare.com/client/v4/accounts/edb167b78c9fb901ea5bca3ce58ccc4b/r2/buckets",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    r3_data = r3.json()
    if r3_data.get("success"):
        buckets = [b["name"] for b in r3_data.get("result", [])]
        print(f"  R2 buckets: {'OK - ' + ', '.join(buckets[:5])}")
    else:
        print(f"  R2 buckets: FAIL - {r3_data.get('errors',[])}")

print("\nDone.")
