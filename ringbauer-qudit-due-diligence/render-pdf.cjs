const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const htmlPath = path.resolve(String.raw`C:\Users\LENOVO\Documents\GitHub\qnfo-research\ringbauer-qudit-due-diligence\ringbauer-qudit-due-diligence.html`);
  const pdfPath = path.resolve(String.raw`C:\Users\LENOVO\Documents\GitHub\qnfo-research\ringbauer-qudit-due-diligence\ringbauer-qudit-due-diligence.pdf`);

  const candidates = [
    String.raw`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`,
    String.raw`C:\Program Files\Microsoft\Edge\Application\msedge.exe`,
    String.raw`C:\Program Files\Google\Chrome\Application\chrome.exe`,
    String.raw`C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`,
  ];
  let executablePath = null;
  const fs = require('fs');
  for (const c of candidates) {
    if (fs.existsSync(c)) { executablePath = c; break; }
  }
  if (!executablePath) {
    console.error('NO CHROMIUM FOUND');
    process.exit(1);
  }
  console.log('using:', executablePath);

  const browser = await puppeteer.launch({
    executablePath,
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 120000 });

  // Wait for MathJax to typeset
  await page.evaluate(async () => {
    if (window.MathJax && MathJax.typesetPromise) {
      await MathJax.typesetPromise();
    }
  });
  await new Promise(r => setTimeout(r, 3000));

  await page.pdf({
    path: pdfPath,
    format: 'A4',
    margin: { top: '2cm', bottom: '2cm', left: '2cm', right: '2cm' },
    printBackground: true
  });
  await browser.close();
  console.log('PDF written to:', pdfPath);
})().catch(e => { console.error('ERROR:', e); process.exit(1); });
