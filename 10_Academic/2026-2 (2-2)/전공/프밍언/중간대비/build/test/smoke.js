const {JSDOM}=require('jsdom'); const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const dom=new JSDOM('<!doctype html><html><head></head><body>'+html+'</body></html>',{runScripts:'dangerously',beforeParse(win){win.scrollTo=()=>{};},url:'https://x.test/',pretendToBeVisual:true});
const w=dom.window; const errs=[];
w.addEventListener('error',e=>errs.push(e.message)); w.console.error=(...a)=>errs.push(a.join(' '));
w.HTMLElement.prototype.scrollIntoView=function(){}; w.CSS={escape:s=>s};
const $=s=>w.document.querySelector(s); const $$=s=>[...w.document.querySelectorAll(s)];
const click=el=>{ if(!el) throw new Error('missing el'); el.dispatchEvent(new w.MouseEvent('click',{bubbles:true})); };
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 await sleep(50);
 console.log('home has CTA:', !!$('.cta'), 'units:', $$('.ucard').length);
 const data=JSON.parse($('#pl-data').textContent); const Q=Object.fromEntries(data.questions.map(q=>[q.id,q]));
 async function answerQuiz(right){
  for(let guard=0;guard<20;guard++){
   const st=JSON.parse(w.localStorage.getItem('pl-learn')); if(st.mode!=='quiz') return st;
   const z=st.quiz; const q=Q[z.items[z.idx].qid];
   if(q.type==='mc'){ click($(`[data-pick="${right?q.answer:(q.answer+1)%q.choices.length}"]`)); click($('[data-submit]')); }
   else if(q.type==='ox'){ click($(`[data-pick="${right?q.answer:!q.answer}"]`)); click($('[data-submit]')); }
   else if(q.type==='blank'){ $$('[data-blank]').forEach((i,k)=>{i.value=right?q.accept[k][0]:'zzz'; i.dispatchEvent(new w.Event('input',{bubbles:true}));}); click($('[data-submit]')); }
   else { const ta=$('textarea'); ta.value='답'; ta.dispatchEvent(new w.Event('input',{bubbles:true})); click($('[data-reveal]')); await sleep(5); click($(`[data-self="${right?1:0}"]`)); }
   await sleep(20);
   click($('[data-qnext]')); await sleep(20);
  }
 }
 click($('[data-lesson="L1-1"]')); await sleep(10);
 console.log('reader sections:', $$('.sec').length, 'title:', $('.rhead h2').textContent);
 click($('[data-startquiz]')); await sleep(10);
 let st=await answerQuiz(true); console.log('after L1-1 quiz mode:', st.mode, 'progress:', w.localStorage.getItem('pl-progress'));
 console.log('summary:', $('.qwrap h2')?.textContent);
 click($('[data-lesson="L1-2"]')); await sleep(10);
 click($('[data-startquiz]')); await sleep(10);
 st=await answerQuiz(false); console.log('L1-2 fail mode:', st.mode, 'review:', JSON.stringify(st.review));
 click($('[data-goreview]')); await sleep(10);
 console.log('banner:', !!$('.banner'), 'highlighted:', $$('.sec.review').length);
 click($('[data-startretest]')); await sleep(10);
 st=JSON.parse(w.localStorage.getItem('pl-learn')); console.log('retest round', st.quiz.round, 'items', st.quiz.items.length);
 st=await answerQuiz(true); console.log('after retest:', st.mode, Object.keys(JSON.parse(w.localStorage.getItem('pl-progress'))));
 console.log('L1-3 unlocked btn disabled?', $('.lrow[data-lesson="L1-3"]').disabled, ' L1-4 disabled?', $('.lrow[data-lesson="L1-4"]').disabled);
 click($('nav.tabs [data-v="practice"]')); await sleep(10); console.log('practice rows', $$('.qrow').length);
 click($$('.qrow')[3]); await sleep(5);
 click($('nav.tabs [data-v="mock"]')); await sleep(10); click($('[data-mockstart]')); await sleep(10); console.log('mock qs', $$('.mockq').length);
 click($('[data-mocksubmit]')); await sleep(100); console.log('mock graded pen', $('.mockhead .pen')?.textContent);
 click($('nav.tabs [data-v="wrong"]')); await sleep(10); console.log('wrong cards', $$('#v-wrong .qwrap').length);
 click($('nav.tabs [data-v="hist"]')); await sleep(10); console.log('hist rows', $$('#v-hist tbody tr').length);
 click($('nav.tabs [data-v="learn"]')); click($('[data-home]')); await sleep(10); console.log('weak list', $$('.wk').length);
 console.log('ERRORS:', errs);
})();
