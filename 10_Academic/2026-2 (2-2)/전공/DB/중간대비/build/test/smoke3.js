const {JSDOM}=require('jsdom'); const fs=require('fs');
const dom=new JSDOM('<!doctype html><html><body>'+fs.readFileSync(process.argv[2],'utf8')+'</body></html>',{runScripts:'dangerously',beforeParse(w){w.scrollTo=()=>{};w.CSS={escape:s=>s};w.HTMLElement.prototype.scrollIntoView=function(){};},url:'https://x.test/'});
const w=dom.window, errs=[]; w.addEventListener('error',e=>errs.push(e.message));
const $=s=>w.document.querySelector(s), click=el=>el&&el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const D=JSON.parse(w.document.querySelector('#db-data').textContent); const Q=Object.fromEntries(D.questions.map(q=>[q.id,q]));
(async()=>{ await sleep(30);
 click($('nav.tabs [data-v="learn"]'));
 for(let round=1;round<=5;round++){
  click($('[data-lesson="L1-1"]')); await sleep(5); click($('[data-startquiz]')); await sleep(5);
  for(let g=0;g<10;g++){ const st=JSON.parse(w.localStorage.getItem('db-learn')); if(st.mode!=='quiz')break;
    const z=st.quiz,q=Q[z.items[z.idx].qid];
    if(q.type==='mc'){click($(`[data-pick="${q.answer}"]`));click($('[data-submit]'));}
    else if(q.type==='ox'){click($(`[data-pick="${q.answer}"]`));click($('[data-submit]'));}
    else if(q.type==='blank'){w.document.querySelectorAll('[data-blank]').forEach((i,k)=>i.value=q.accept[k][0]);click($('[data-submit]'));}
    else {click($('[data-reveal]'));await sleep(3);click($('[data-self="1"]'));}
    await sleep(10); click($('[data-qnext]')); await sleep(10); }
  await sleep(10);
  const st=JSON.parse(w.localStorage.getItem('db-learn'));
  console.log('round',round,'mode',st.mode,'carried',Object.values(st.quiz.res).filter(r=>r.carried).length,'/',st.quiz.items.length);
 }
 console.log('ERRORS',errs);
})();
