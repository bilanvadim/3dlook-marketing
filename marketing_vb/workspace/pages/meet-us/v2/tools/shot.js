// node tools/shot.js <html> <out.png> <width> [height] [evalJS]
const {chromium}=require(process.env.HOME+'/.local/lib/node_modules/@playwright/mcp/node_modules/playwright');
(async()=>{
  const [,,file,out,w,h,ev]=process.argv;
  const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
  const p=await b.newPage({viewport:{width:+w,height:+(h||900)},deviceScaleFactor:1});
  await p.goto('file://'+require('path').resolve(file));
  await p.waitForTimeout(300);
  if(ev) await p.evaluate(ev);
  await p.waitForTimeout(200);
  await p.screenshot({path:out,fullPage:!h});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
