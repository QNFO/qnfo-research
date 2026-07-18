"""D1 backfill + DNSLink creation via wrangler CLI (with --remote)."""
import subprocess, os, sys

BASE = r"C:\Users\LENOVO\AppData\Local\Programs\DeepChat"
ZONE_ID = "d6d1e08f7e9405a9cfa3d8f4630c9b0c"

PAPERS = [
    {
        "slug": "silent-radix-synthesis",
        "cid": "QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS",
        "dns_name": "_dnslink.silent-radix-cryptography",
        "title": "Silent-Radix Cryptography",
    },
    {
        "slug": "syntactic-generation-primitive-distinctions",
        "cid": "QmRLFE9iwokBuU1s4EYAkEUqGcABix1CnMBxcoht4n3JoH",
        "dns_name": "_dnslink.syntactic-generation-primitive-distinctions",
        "title": "Syntactic Generation Primitive Distinctions",
    },
    {
        "slug": "paper-the-qubit-delusion",
        "cid": "QmZVcTQ4Szud3M1LULGLa1aWss55ciZk8db1QvwRC4wJt2",
        "dns_name": "_dnslink.the-qubit-delusion",
        "title": "The Qubit Delusion",
    },
    {
        "slug": "paper-beyond-the-qubit",
        "cid": "QmezmA2Ejo3t8DYGseFJhECrm2QCCaa3GQc2N7RMJSTuEw",
        "dns_name": "_dnslink.beyond-the-qubit",
        "title": "Beyond the Qubit",
    },
    {
        "slug": "number-theoretic-ultrametric-foundations",
        "cid": "QmUtD9P2BDYMSaaz7WFTBPEmK9ViMkqj8iR6HjkWChm4i8",
        "dns_name": "_dnslink.number-theoretic-ultrametric-foundations",
        "title": "Number-Theoretic Ultrametric Foundations",
    },
]

def run_cmd(cmd, timeout=45):
    result = subprocess.run(cmd, cwd=BASE, capture_output=True, text=True, timeout=timeout, shell=True)
    return result.returncode == 0, (result.stdout + result.stderr)

# === D1 BACKFILL ===
print("=" * 60)
print("D1 BACKFILL (living-paper)")
print("=" * 60)

now = "2026-07-18T00:00:00Z"
d1_success = 0
d1_fail = 0

for p in PAPERS:
    # Escape single quotes in SQL
    sql = f"UPDATE papers SET distribution_status='distributed', ipfs_cid='{p['cid']}', updated_at='{now}' WHERE slug='{p['slug']}'"
    print(f"\n{p['slug']}: ", end="", flush=True)

    # Use double-quotes around SQL to avoid escaping issues
    cmd = f'npx wrangler d1 execute living-paper --remote --command="{sql}"'
    ok, out = run_cmd(cmd, timeout=45)

    if ok and "ERROR" not in out:
        # Check for actual success
        if "rows matched" in out.lower() or "OK" in out:
            print("OK")
            d1_success += 1
        elif "no rows" in out.lower():
            print(f"NO MATCH (slug might not exist in D1)")
            d1_fail += 1
        else:
            print(f"OK (no error)")
            d1_success += 1
    else:
        # Extract error
        lines = out.strip().split("\n")
        error_lines = [l for l in lines if "error" in l.lower() or "ERROR" in l]
        print(f"FAIL: {'; '.join(error_lines[:3])[:200]}")
        d1_fail += 1

print(f"\nD1: {d1_success}/{len(PAPERS)} updates, {d1_fail} failed")

# === DNSLink RECORDS ===
print("\n" + "=" * 60)
print("DNSLink TXT RECORDS")
print("=" * 60)

dns_success = 0
dns_fail = 0

for p in PAPERS:
    dnslink = f"dnslink=/ipfs/{p['cid']}"
    fqdn = f"{p['dns_name']}.qnfo.org"
    print(f"\n{fqdn} -> {dnslink}: ", end="", flush=True)

    cmd = f'npx wrangler dns record create "{p["dns_name"]}" --zone-id {ZONE_ID} --type TXT --content "{dnslink}" --ttl 3600 --comment "Core pillar paper - WBS.3"'
    ok, out = run_cmd(cmd, timeout=45)

    if ok:
        print("OK")
        dns_success += 1
    else:
        if "already exists" in out.lower() or "duplicate" in out.lower() or "81057" in out:
            print("SKIP (already exists)")
            dns_success += 1
        else:
            # Extract error
            lines = out.strip().split("\n")
            error_lines = [l for l in lines if "error" in l.lower() or "ERROR" in l]
            print(f"FAIL: {'; '.join(error_lines[:3])[:200]}")
            dns_fail += 1

print(f"\nDNS: {dns_success}/{len(PAPERS)} records, {dns_fail} failed")
print("\nDone.")
