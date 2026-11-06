// node tools/render_video.js out/video-foyer.html out/route-foyer.mp4 [fps]
const {chromium}=require(process.env.HOME+'/.local/lib/node_modules/@playwright/mcp/node_modules/playwright');
const {spawn}=require('child_process'); const path=require('path');
(async()=>{
  const [,,file,out,fpsArg]=process.argv; const fps=+(fpsArg||30);
  const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});
  const p=await b.newPage({viewport:{width:+(process.env.VW||1080),height:+(process.env.VH||1080)},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(file)); await p.waitForTimeout(400);
  const dur=await p.evaluate(()=>window.__duration);
  const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(fps),'-i','-',
    '-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-movflags','+faststart',out],{stdio:['pipe','inherit','inherit']});
  const n=Math.round(dur*fps);
  for(let i=0;i<n;i++){
    await p.evaluate(t=>window.__frame(t), i/fps);
    const buf=await p.screenshot({type:'png'});
    if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
  }
  ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close();
  console.log(out, n, 'frames', dur.toFixed(1)+'s');
})().catch(e=>{console.error(e);process.exit(1)});
