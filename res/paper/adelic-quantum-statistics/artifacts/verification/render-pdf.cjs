// render-pdf.cjs — QNFO.RES.024: CDP PDF render + DOM checks (2026-08-26).
// Canonical pipeline: pandoc --mathjax HTML -> Edge headless -> page.pdf (PDF-PATH-OPTION-1: path required).
const puppeteer = require('C:/Users/LENOVO/node_modules/puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  const htmlPath = path.resolve(__dirname, '..', '..', 'adelic-quantum-statistics.html');
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'load', timeout: 60000 });
  await new Promise(r => setTimeout(r, 4000)); // MathJax settle
  const checks = await page.evaluate(() => ({
    merrorCount: document.querySelectorAll('merror, .MathJax_Error, [data-mjx-error]').length,
    fffd: document.body.innerText.includes('\uFFFD'),
    h1title: document.querySelectorAll('h1.title').length,
    bodyH1: document.querySelectorAll('body h1:not(.title)').length,
    refs: document.querySelectorAll('#refs .csl-entry, div.csl-entry').length,
    abstractDivs: document.querySelectorAll('div.abstract').length,
  }));
  const pdfPath = path.resolve(__dirname, '..', '..', 'adelic-quantum-statistics.pdf');
  await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, displayHeaderFooter: false });
  console.log('DOM-CHECKS', JSON.stringify(checks));
  console.log('PDF-PATH', pdfPath);
  await browser.close();
})().catch(e => { console.error('RENDER-FAIL', e); process.exit(1); });
