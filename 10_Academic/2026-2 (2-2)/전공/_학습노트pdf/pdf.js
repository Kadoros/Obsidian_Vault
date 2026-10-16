const { chromium } = require("playwright"); const fs = require("fs");
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch();
  for (const [hp, out, title] of jobs){
    const p = await b.newPage(); const miss = [];
    p.on("requestfailed", r => miss.push(r.url()));
    await p.goto("file://" + hp, { waitUntil:"networkidle" }); await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: out, format:"A4", printBackground:true, displayHeaderFooter:true,
      headerTemplate:"<span></span>",
      footerTemplate:`<div style="width:100%;font-size:8px;color:#888;padding:0 15mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>${title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      margin:{ top:"16mm", bottom:"18mm", left:"15mm", right:"15mm" } });
    const imgs = await p.evaluate(() => [...document.images].filter(i => !i.naturalWidth).map(i => i.src));
    console.log(out.split("/").pop(), "broken imgs:", imgs.length, "failed:", miss.length);
  }
  await b.close();
})();
