// node tools/frame.js out/map-foyer.html out/poster.png 8.5   -> one frame at t seconds
const {chromium}=require(process.env.HOME+'/.local/lib/node_modules/@playwright/mcp/node_modules/playwright');
const path=require('path');
(async()=>{
  const [,,file,out,t]=process.argv;
  const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
  const p=await b.newPage({viewport:{width:+(process.env.VW||1600),height:+(process.env.VH||1270)},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(file)+'#render'); await p.waitForTimeout(400);
  await p.evaluate(t=>window.__frame(t), +(t||0));
  await p.screenshot({path:out}); await b.close(); console.log(out);
})().catch(e=>{console.error(e);process.exit(1)});
