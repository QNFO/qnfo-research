"""Upload all 10 core pillar files to R2 via wrangler CLI."""
import subprocess, os, sys

BASE = r"C:\Users\LENOVO\AppData\Local\Programs\DeepChat"

uploads = [
    ("silent-radix", "silent-radix-cryptography.pdf", "releases/core-pillars/silent-radix/silent-radix-cryptography.pdf"),
    ("silent-radix", "silent-radix-cryptography.md", "releases/core-pillars/silent-radix/silent-radix-cryptography.md"),
    ("syntactic-primitive", "syntactic-generation-primitive-distinctions.pdf", "releases/core-pillars/syntactic-primitive/syntactic-generation-primitive-distinctions.pdf"),
    ("syntactic-primitive", "syntactic-generation-primitive-distinctions.md", "releases/core-pillars/syntactic-primitive/syntactic-generation-primitive-distinctions.md"),
    ("qubit-delusion", "the-qubit-delusion.pdf", "releases/core-pillars/qubit-delusion/the-qubit-delusion.pdf"),
    ("qubit-delusion", "the-qubit-delusion.md", "releases/core-pillars/qubit-delusion/the-qubit-delusion.md"),
    ("beyond-qubit", "beyond-the-qubit.pdf", "releases/core-pillars/beyond-qubit/beyond-the-qubit.pdf"),
    ("beyond-qubit", "beyond-the-qubit.md", "releases/core-pillars/beyond-qubit/beyond-the-qubit.md"),
    ("ultrametric", "number-theoretic-ultrametric-foundations.pdf", "releases/core-pillars/ultrametric-foundations/number-theoretic-ultrametric-foundations.pdf"),
    ("ultrametric", "number-theoretic-ultrametric-foundations.md", "releases/core-pillars/ultrametric-foundations/number-theoretic-ultrametric-foundations.md"),
]

success = 0
failed = 0

for slug, fname, local_path in uploads:
    full_local = os.path.join(BASE, local_path)
    r2_key = f"releases/2026/07/core-pillars/{slug}/{fname}"

    if not os.path.exists(full_local):
        print(f"MISSING: {full_local}")
        failed += 1
        continue

    print(f"Uploading: {r2_key} ({os.path.getsize(full_local):,} bytes)...", end=" ", flush=True)

    result = subprocess.run(
        f'npx wrangler r2 object put "qnfo-releases/{r2_key}" --file "{full_local}"',
        cwd=BASE,
        capture_output=True,
        text=True,
        timeout=60,
        shell=True,
    )

    if result.returncode == 0 and "Upload complete" in result.stdout:
        print("OK")
        success += 1
    else:
        print(f"FAIL ({result.returncode})")
        if result.stderr:
            print(f"  stderr: {result.stderr[:200]}")
        failed += 1

print(f"\n{'='*60}")
print(f"R2 Uploads: {success}/{len(uploads)} success, {failed}/{len(uploads)} failed")
print(f"{'='*60}")
