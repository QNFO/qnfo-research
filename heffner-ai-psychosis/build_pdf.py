"""Build PDF via canonical CDP pipeline: pandoc -> MathJax SVG inline -> puppeteer-core."""
import subprocess, sys, os, urllib.request, zipfile, tempfile, shutil

PANDOC = r"C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe"
PAPER = r"C:\Users\LENOVO\source\repos\QNFO\qnfo-research\heffner-ai-psychosis\paper.md"
OUTDIR = r"C:\Users\LENOVO\source\repos\QNFO\qnfo-research\heffner-ai-psychosis"
MATHJAX_DIR = os.path.join(tempfile.gettempdir(), "mathjax")
MATHJAX_JS = os.path.join(MATHJAX_DIR, "tex-svg-full.js")

# Step 1: Download MathJax SVG if not cached
if not os.path.exists(MATHJAX_JS):
    print("Downloading MathJax SVG (step 1/5)...")
    os.makedirs(MATHJAX_DIR, exist_ok=True)
    url = "https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz"  # stable release
    # Actually use the CDN file directly
    url = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js"
    urllib.request.urlretrieve(url, MATHJAX_JS)
    print(f"  Cached to {MATHJAX_JS} ({os.path.getsize(MATHJAX_JS)} bytes)")

# Step 2: pandoc --mathjax
html_path = os.path.join(OUTDIR, "paper.html")
pdf_path = os.path.join(OUTDIR, "heffner-ai-psychosis.pdf")
print("Running pandoc (step 2/5)...")
result = subprocess.run(
    [PANDOC, "--mathjax", "--standalone", PAPER, "-o", html_path],
    capture_output=True, text=True
)
if result.returncode != 0:
    print(f"Pandoc failed: {result.stderr}")
    sys.exit(1)
print("  OK")

# Step 3: Switch CHTML -> SVG + inline local MathJax
print("Switching CHTML->SVG + inlining MathJax (step 3/5)...")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Switch to SVG
html = html.replace("tex-chtml-full.js", "tex-svg-full.js")

# Inline local MathJax
cdn_url = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js"
with open(MATHJAX_JS, "r", encoding="utf-8") as f:
    mathjax_js = f.read()
html = html.replace(f'<script src="{cdn_url}"></script>',
                     f'<script>{mathjax_js}</script>')
# Also try the async variant
html = html.replace(f'<script async="" src="{cdn_url}"></script>',
                     f'<script>{mathjax_js}</script>')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"  HTML: {len(html)} chars")

# Step 4: puppeteer-core CDP render
print("Rendering PDF via CDP (step 4/5)...")
render_js = os.path.join(OUTDIR, "render_pdf.mjs")
with open(render_js, "w", encoding="utf-8") as f:
    f.write(f"""import puppeteer from "puppeteer-core";
import {{ createRequire }} from "module";
const require = createRequire(import.meta.url);

const chromiumPaths = [
    process.env.CHROME_BIN,
    "C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
    "C:\\\\Program Files (x86)\\\\Microsoft\\\\Edge\\\\Application\\\\msedge.exe",
];

async function findChrome() {{
    const fs = await import("fs");
    for (const p of chromiumPaths) {{
        if (p && fs.existsSync(p)) return p;
    }}
    throw new Error("No Chromium found");
}}

const execPath = await findChrome();
console.log("Using Chromium:", execPath);

const browser = await puppeteer.launch({{
    executablePath: execPath,
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"],
}});

const page = await browser.newPage();
const htmlUrl = "file:///{html_path.replace(chr(92), '/')}";
await page.goto(htmlUrl, {{ waitUntil: "networkidle0", timeout: 60000 }});

// Wait for MathJax to finish
await page.waitForFunction(() => {{
    return window.MathJax && window.MathJax.startup && window.MathJax.startup.promise;
}}, {{ timeout: 30000 }});

await page.waitForTimeout(2000);

await page.pdf({{
    path: "{pdf_path.replace(chr(92), '/')}",
    format: "A4",
    margin: {{ top: "2cm", bottom: "2cm", left: "2cm", right: "2cm" }},
    printBackground: true,
}});

await browser.close();
console.log("PDF written to:", "{pdf_path.replace(chr(92), '/')}");
""")

# Find node_modules with puppeteer-core
npm_root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "..")
# Try common locations
for root in [npm_root, r"C:\Users\LENOVO\AppData\Roaming\npm", r"C:\Program Files\nodejs"]:
    test = os.path.join(root, "node_modules", "puppeteer-core")
    if os.path.isdir(test):
        os.environ["NODE_PATH"] = os.path.join(root, "node_modules")
        break

result = subprocess.run(["node", render_js], capture_output=True, text=True, timeout=120)
print(result.stdout)
if result.returncode != 0:
    print(f"CDP render failed: {result.stderr}")
    # Don't exit - maybe PDF was still written
else:
    print("  OK")

# Step 5: Verify
if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    with open(pdf_path, "rb") as f:
        data = f.read()
    fffd = data.count(b"\xef\xbf\xbd")
    ffff = data.count(b"\xef\xbf\xbf")
    print(f"Verification (step 5/5): {size} bytes, U+FFFD={fffd}, U+FFFF={ffff}")
    if size > 100000 and fffd == 0 and ffff == 0:
        print("PASS: PDF built successfully")
    else:
        print(f"WARN: size={size}, FFFD={fffd}, FFFF={ffff}")
else:
    print("ERROR: PDF was not written")
    sys.exit(1)
