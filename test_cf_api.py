"""Test Cloudflare account-level API token scopes."""
import os, requests

token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
ZONE = "d6d1e08f7e9405a9cfa3d8f4630c9b0c"
ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"

headers = {"Authorization": f"Bearer {token}"}

# Test account
r = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}", headers=headers, timeout=10)
print(f"Account: {r.status_code} success={r.json().get('success')}")

# Test zone
r = requests.get(f"https://api.cloudflare.com/client/v4/zones/{ZONE}", headers=headers, timeout=10)
d = r.json()
print(f"Zone: {r.status_code} success={d.get('success')}")
if d.get("success"):
    print(f"  name={d['result']['name']}")

# Test DNS records
r = requests.get(f"https://api.cloudflare.com/client/v4/zones/{ZONE}/dns_records?per_page=3", headers=headers, timeout=10)
d = r.json()
print(f"DNS list: {r.status_code} success={d.get('success')}")
if d.get("success"):
    print(f"  count={len(d['result'])}")
    for rec in d["result"][:3]:
        print(f"  {rec['type']} {rec['name']}.{rec.get('zone_name','')} -> {rec['content'][:50]}")
else:
    print(f"  errors={d.get('errors')}")

# Test DNS create
rn = f"_dnslink.test-wbs3-verify"
r = requests.post(
    f"https://api.cloudflare.com/client/v4/zones/{ZONE}/dns_records",
    headers={**headers, "Content-Type": "application/json"},
    json={"type": "TXT", "name": rn, "content": "test-dnslink-record", "ttl": 60},
    timeout=10,
)
d = r.json()
print(f"DNS create: {r.status_code} success={d.get('success')}")
if d.get("success"):
    rid = d["result"]["id"]
    print(f"  created id={rid}")
    # Cleanup
    requests.delete(f"https://api.cloudflare.com/client/v4/zones/{ZONE}/dns_records/{rid}", headers=headers, timeout=10)
    print(f"  cleaned up")
else:
    print(f"  errors={d.get('errors')}")
