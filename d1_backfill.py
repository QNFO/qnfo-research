"""Update D1 paper records via qnfo-gateway /sync endpoint with IPFS CIDs and distribution status."""
import os, json, requests, datetime

GATEWAY = "https://graph-api.qnfo.org"
now = datetime.datetime.utcnow().isoformat() + "Z"

# Paper updates with IPFS CIDs
updates = [
    {
        "slug": "silent-radix-synthesis",
        "ipfs_cid": "QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS",
        "ipfs_cid_md": "QmafHkGCdmGaQE4JHVj4J9zop2Xzj1rLtPudW6kpuXvb79",
        "dist_status": "distributed",
        "title": "Silent-Radix Cryptography: Exploiting the Base Ambiguity of Positional Notation as a Cryptographic Primitive",
    },
    {
        "slug": "syntactic-generation-primitive-distinctions",
        "ipfs_cid": "QmRLFE9iwokBuU1s4EYAkEUqGcABix1CnMBxcoht4n3JoH",
        "ipfs_cid_md": "QmeGBjdfX93ZM3hBSo5PxcYFPtoqiC1U7TmqXxDUNpFpVm",
        "dist_status": "distributed",
        "title": "Syntactic Generation Primitive Distinctions",
    },
    {
        "slug": "paper-the-qubit-delusion",
        "ipfs_cid": "QmZVcTQ4Szud3M1LULGLa1aWss55ciZk8db1QvwRC4wJt2",
        "ipfs_cid_md": "QmbGponfgMfyCsrRe8ugHBkfffSzrm2q3Pu1qhYEJUNJnx",
        "dist_status": "distributed",
        "title": "The Qubit Delusion",
    },
    {
        "slug": "paper-beyond-the-qubit",
        "ipfs_cid": "QmezmA2Ejo3t8DYGseFJhECrm2QCCaa3GQc2N7RMJSTuEw",
        "ipfs_cid_md": "QmYyXcoFxV2e7wFjBDVkpWLnZfn3v1PHEKDVE4pkHs8etq",
        "dist_status": "distributed",
        "title": "Beyond the Qubit",
    },
    {
        "slug": "number-theoretic-ultrametric-foundations",
        "ipfs_cid": "QmUtD9P2BDYMSaaz7WFTBPEmK9ViMkqj8iR6HjkWChm4i8",
        "ipfs_cid_md": "QmUw8PezufWDQmLWh1X1NdDgTEnkZgn7Hh1JeZ8ckVdeBU",
        "dist_status": "distributed",
        "title": "Number-Theoretic Ultrametric Foundations",
    },
]

results = {"success": 0, "failed": 0, "details": []}

for u in updates:
    slug = u["slug"]
    print(f"\nUpdating: {slug}...")

    # Approach: Use direct D1 SQL UPDATE via /query endpoint
    sql = f"""
    UPDATE papers SET 
        ipfs_cid = '{u["ipfs_cid"]}',
        ipfs_cid_md = '{u["ipfs_cid_md"]}',
        distribution_status = '{u["dist_status"]}',
        updated_at = '{now}'
    WHERE slug = '{slug}'
    """

    try:
        r = requests.post(
            f"{GATEWAY}/query",
            json={"query": sql},
            timeout=15,
        )
        data = r.json()
        if "error" in data:
            print(f"  FAIL (query): {data['error']}")
            results["failed"] += 1
            results["details"].append({"slug": slug, "status": "failed", "error": data["error"]})

            # Try alternate: /sync with nodes
            print(f"  Trying /sync fallback...")
            node = {
                "id": f"paper-{slug}",
                "name": u["title"],
                "label": "Paper",
                "properties": json.dumps({
                    "slug": slug,
                    "ipfs_cid": u["ipfs_cid"],
                    "ipfs_cid_md": u["ipfs_cid_md"],
                    "distribution_status": u["dist_status"],
                    "updated_at": now,
                }),
            }
            r2 = requests.post(
                f"{GATEWAY}/sync",
                json={"action": "bulk", "nodes": [node], "edges": []},
                timeout=15,
            )
            d2 = r2.json()
            if d2.get("success"):
                print(f"  OK (via /sync)")
                results["success"] += 1
                results["details"].append({"slug": slug, "status": "ok", "method": "sync"})
            else:
                print(f"  FAIL (sync): {d2}")
                results["details"].append({"slug": slug, "status": "failed_sync", "error": str(d2)})
        else:
            print(f"  OK (via /query)")
            results["success"] += 1
            results["details"].append({"slug": slug, "status": "ok", "method": "query"})

    except Exception as e:
        print(f"  ERROR: {e}")
        results["failed"] += 1
        results["details"].append({"slug": slug, "status": "error", "error": str(e)})

print(f"\n=== RESULTS ===")
print(f"Success: {results['success']}/{len(updates)}")
print(f"Failed: {results['failed']}/{len(updates)}")

# Verify
print("\n=== VERIFICATION ===")
for u in updates:
    try:
        r = requests.get(
            f"https://graph-api.qnfo.org/nodes/{u['slug']}",
            timeout=10,
        )
        if r.status_code == 200:
            node = r.json()
            props = node.get("properties", {})
            status = props.get("distribution_status", "unknown")
            cid = props.get("ipfs_cid", "none")
            print(f"  {u['slug']}: status={status}, cid={cid[:20]}...")
        else:
            print(f"  {u['slug']}: HTTP {r.status_code}")
    except Exception as e:
        print(f"  {u['slug']}: ERROR {e}")

print("\nDone.")
