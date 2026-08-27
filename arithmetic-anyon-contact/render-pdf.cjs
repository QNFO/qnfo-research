// render-pdf.cjs — QNFO.RES.028 publication PDF build (CDP, no browser chrome).
// Usage: NODE_PATH=C:\Users\LENOVO\npm-global\node_modules node render-pdf.cjs <in.html> <out.pdf>
const puppeteer = require('puppeteer-core');

(async () => {
  const exe = process.env.EDGE_EXE ||
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const browser = await puppeteer.launch({
    executablePath: exe,
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1240, height: 1754 });
  const url = 'file://' + process.argv[2].replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 120000 });
  // wait for MathJax typesetting to settle
  await page.evaluate(async () => {
    if (window.MathJax && window.MathJax.typesetPromise) {
      await window.MathJax.typesetPromise();
    }
  }).catch(() => {});
  await new Promise(r => setTimeout(r, 3000));
  await page.pdf({
    path: process.argv[3],
    format: 'A4',
    displayHeaderFooter: false,       // PDF-NO-BROWSER-CHROME-1: explicit
    margin: { top: '2cm', bottom: '2cm', left: '2cm', right: '2cm' },
    printBackground: true,
  });
  await browser.close();
  console.log('PDF written:', process.argv[3]);
})().catch(e => { console.error('RENDER FAILED:', e.message); process.exit(1); });
