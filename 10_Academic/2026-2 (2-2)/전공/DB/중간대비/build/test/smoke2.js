const {JSDOM}=require('jsdom'); const fs=require('fs');
const dom=new JSDOM('<!doctype html><html><body>'+fs.readFileSync(process.argv[2],'utf8')+'</body></html>',{runScripts:'dangerously',beforeParse(w){w.scrollTo=()=>{};w.HTMLElement.prototype.scrollIntoView=function(){};},url:'https://x.test/'});
const w=dom.window, errs=[]; w.addEventListener('error',e=>errs.push(e.message));
const $=s=>w.document.querySelector(s), click=el=>el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
setTimeout(()=>{
 click($('nav.tabs [data-v="dash"]'));
 console.log('stats',w.document.querySelectorAll('#v-dash .stat').length,'rows',w.document.querySelectorAll('#v-dash tbody tr').length,'recs',w.document.querySelectorAll('.rec').length);
 click($('[data-plesson="L3-4"]')); console.log('practice rows',w.document.querySelectorAll('.qrow').length, !!$('[data-clearlesson]'));
 click($('nav.tabs [data-v="learn"]')); click($('[data-lesson="L1-1"]')); click($('[data-startquiz]'));
 const st=JSON.parse(w.localStorage.getItem('db-learn')); const d=JSON.parse($('#db-data').textContent); const q=d.questions.find(x=>x.id===st.quiz.items[0].qid);
 console.log('first q type',q.type,'badge before',!!$('.prev'));
 console.log('ERRORS',errs);
},50);
