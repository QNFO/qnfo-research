"""Build PDF: skip MathJax (paper has minimal math), pandoc -> CDP directly."""
import subprocess, sys, os

PANDOC = r"C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe"
PAPER = r"C:\Users\LENOVO\source\repos\QNFO\qnfo-research\heffner-ai-psychosis\paper.md"
OUTDIR = r"C:\Users\LENOVO\source\repos\QNFO\qnfo-research\heffner-ai-psychosis"
html_path = os.path.join(OUTDIR, "paper.html")
pdf_path = os.path.join(OUTDIR, "heffner-ai-psychosis.pdf")

# Step 1: pandoc with --katex for math (pre-rendered, no JS needed)
# Actually, just use basic HTML - this paper has essentially zero math
print("Step 1: pandoc...")
subprocess.run([PANDOC, "--standalone", PAPER, "-o", html_path], check=True)
print("  OK")

# Step 2: Inject basic CSS for readability
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

css = """
<style>
body { font-family: 'Georgia', 'Times New Roman', serif; font-size: 12pt; line-height: 1.6; max-width: 42em; margin: 0 auto; padding: 2em; color: #1a1a1a; }
h1 { font-size: 1.8em; margin-top: 0; }
h2 { font-size: 1.4em; margin-top: 1.5em; }
h3 { font-size: 1.2em; }
p { margin: 0.8em 0; text-align: justify; hyphens: auto; }
code { font-family: 'Consolas', monospace; font-size: 0.9em; background: #f5f5f5; padding: 0.1em 0.3em; border-radius: 3px; }
pre { background: #f5f5f5; padding: 1em; border-radius: 4px; overflow-x: auto; font-size: 0.9em; line-height: 1.4; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 1em; color: #555; font-style: italic; }
a { color: #0066cc; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #ddd; padding: 0.5em; text-align: left; }
th { background: #f5f5f5; }
@media print { body { font-size: 11pt; } }
</style>
"""
html = html.replace("</head>", css + "</head>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"  HTML: {len(html)} chars")

# Step 3: CDP render
print("Step 3: CDP render...")
render_js = os.path.join(OUTDIR, "render_pdf.mjs")
with open(render_js, "w", encoding="utf-8") as f:
    f.write(f"""import puppeteer from "puppeteer-core";
import fs from "fs";

const paths = [
    "C:\\\\Program Files (x86)\\\\Microsoft\\\\Edge\\\\Application\\\\msedge.exe",
    "C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
];
const execPath = paths.find(p => fs.existsSync(p));
if (!execPath) throw new Error("No Chromium");
console.log("Chromium:", execPath);

const browser = await puppeteer.launch({{
    executablePath: execPath, headless: true,
    args: ["--no-sandbox", "--disable-gpu"],
}});

const page = await browser.newPage();
await page.goto("file:///{html_path.replace(chr(92), '/')}", {{ waitUntil: "networkidle0", timeout: 60000 }});
await new Promise(r => setTimeout(r, 1000));

await page.pdf({{
    path: "{pdf_path.replace(chr(92), '/')}",
    format: "A4",
    margin: {{ top: "2cm", bottom: "2cm", left: "2cm", right: "2cm" }},
    printBackground: true,
}});

await browser.close();
console.log("PDF written");
""")

result = subprocess.run(["node", render_js], capture_output=True, text=True, timeout=120)
print(result.stdout)
if result.returncode != 0:
    print("STDERR:", result.stderr[:400])

# Step 4: Verify
if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    with open(pdf_path, "rb") as f:
        data = f.read()
    fffd = data.count(b"\xef\xbf\xbd")
    ffff = data.count(b"\xef\xbf\xbf")
    print(f"PDF: {size} bytes, U+FFFD={fffd}, U+FFFF={ffff}")
    if size > 50000 and fffd == 0 and ffff == 0:
        print("PASS")
    else:
        print("GATE ISSUE")
else:
    print("FAIL: PDF not written")
    sys.exit(1)
