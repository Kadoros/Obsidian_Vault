// Claude 채점·db 기록·코스 경로 스모크 테스트 (가짜 window.claude 사용)
// node test/smoke_claude.js page.html bank.json learn.json
const { JSDOM } = require("jsdom"); const fs = require("fs"); const { install } = require("./fake_claude");
const html = fs.readFileSync(process.argv[2], "utf8"), bankTxt = fs.readFileSync(process.argv[3], "utf8"), learnTxt = fs.readFileSync(process.argv[4], "utf8");
const sleep = ms => new Promise(r => setTimeout(r, ms));
let fails = 0; const ok = (c, msg) => { console.log((c ? "PASS " : "FAIL ") + msg); if (!c) fails++; };
const COURSE = { title: "테스트 코스", since: 1, steps: [{ qid: "2025-2", stage: "1단계", goal: "목표" }, { qid: "2025-3", stage: "1단계", goal: "목표2" }] };

async function boot(mode, seed = {}){
  let fake;
  const dom = new JSDOM("<!doctype html><html><body>" + html + "</body></html>", { runScripts: "dangerously", url: "https://x.test/",
    beforeParse(w){ w.scrollTo = () => {}; w.requestAnimationFrame = f => setTimeout(f, 0); w.HTMLElement.prototype.scrollIntoView = function(){};
      w.fetch = async u => ({ json: async () => JSON.parse(String(u).includes("learn") ? learnTxt : bankTxt) });
      fake = install(w, { mode, seed }); } });
  const w = dom.window, errs = []; w.addEventListener("error", e => errs.push(e.message));
  const $ = s => w.document.querySelector(s);
  const click = el => { if (!el) throw new Error("missing element"); el.dispatchEvent(new w.MouseEvent("click", { bubbles: true })); };
  const go = qid => { const b = w.document.createElement("button"); b.dataset.go = qid; w.document.body.appendChild(b); click(b); b.remove(); };
  const type = (el, v) => { el.value = v; el.dispatchEvent(new w.Event("input", { bubbles: true })); };
  await sleep(300);  // 학습 탭이 붙어서 jsdom 파싱이 느려짐
  return { w, $, click, go, type, errs, fake };
}

(async () => {
  // 1) 정상 채점 + 변형문제 + 코스
  let t = await boot("ok", { extra_questions: { "x-1": { prompt: "EXTRA_Q_MARKER", answer: "a", topics: ["static"] } }, course: { current: COURSE } });
  ok(t.$("#grader").textContent.includes("Claude"), "sample 연결 → 채점 칩 'Claude'");
  ok(t.$("#store").textContent.includes("클라우드"), "db 연결 → 저장 칩 '클라우드'");
  ok(!t.$("#tab-course").hidden && t.$("#v-course").textContent.includes("테스트 코스"), "course/current → 코스 탭 표시");
  t.go("2025-8"); await sleep(10);
  t.type(t.$("#ans"), "class A { int x; };"); t.click(t.$("#b-grade")); await sleep(60);
  let at = Object.values(t.fake.store.attempts || {});
  ok(at.length === 1 && at[0].grader === "claude" && at[0].score === 0.8 && at[0].mode === "practice", "코드 문제 Claude 채점 → attempts에 저장");
  ok(t.fake.calls[0]?.opts?.modelTier === "default" && t.fake.calls[0].prompt.includes("class A"), "code는 default 티어, 학생 답이 프롬프트에 들어감");
  ok(t.$("#res .fb")?.textContent.includes("가짜 채점"), "점수·피드백 화면 표시");
  t.click(t.$('[data-self="0"]')); await sleep(20);
  at = Object.values(t.fake.store.attempts);
  ok(at.length === 1 && at[0].grader === "claude+self" && at[0].score === 0, "자가채점 수정 → 같은 기록 update");
  t.go("2025-2"); await sleep(10);
  t.type(t.$("#ans"), "short answer"); t.click(t.$("#b-grade")); await sleep(60);
  ok(t.fake.calls[1]?.opts?.modelTier === "quick", "short는 quick 티어");
  t.go("x-1"); await sleep(10);
  ok(t.w.document.body.textContent.includes("EXTRA_Q_MARKER"), "extra_questions 병합");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  // 2) 채점 실패 → 안내 + 자가채점 폴백
  t = await boot("rate_limited");
  t.go("2025-8"); await sleep(10);
  t.type(t.$("#ans"), "아무 답"); t.click(t.$("#b-grade")); await sleep(60);
  ok(t.$("#res .err")?.textContent.includes("몰렸어"), "rate_limited 안내 문구");
  ok(!Object.keys(t.fake.store.attempts || {}).length, "실패한 채점은 기록 안 함");
  t.click(t.$('[data-self="0.5"]')); await sleep(20);
  at = Object.values(t.fake.store.attempts || {});
  ok(at.length === 1 && at[0].grader === "self" && at[0].score === 0.5, "자가채점 폴백 기록");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  // 3) 학습 탭: 레슨 읽기 → 점검 → 틀리면 복습 → 재시험, 기록은 checks/progress에 (attempts와 분리)
  t = await boot("ok");
  const L = JSON.parse(learnTxt);
  t.click(t.$('nav.tabs [data-v="learn"]')); await sleep(10);
  ok(t.$("#v-learn .tree") && t.$("#v-learn").textContent.includes("학습 홈"), "학습 탭 홈 표시");
  ok(t.w.document.querySelectorAll("#v-learn .tree .lrow[data-lesson]").length === L.units.reduce((s,u)=>s+u.lessons.length,0), "트리에 레슨 전부");
  t.click(t.$('#v-learn [data-lesson="L4-5"]')); await sleep(10);
  ok(t.$("#v-learn .reader h2")?.textContent.length > 0 && t.$("#s-shallow-deep"), "레슨 L4-5 본문 표시");
  ok(t.$('#v-learn [data-topic="copy"]'), "관련 기출 버튼 (copy)");
  const lid = "L4-5", ncon = L.units.flatMap(u=>u.lessons).find(l=>l.id===lid).secs.length;
  t.click(t.$('[data-lquiz="L4-5"]')); await sleep(10);
  ok(t.$("#v-learn .qwrap") && t.w.document.querySelectorAll("#v-learn .pips i").length === ncon*2, "점검 시작: 개념당 2문제");
  // 전부 틀리게 답하기
  for (let i = 0; i < ncon*2; i++){
    const skip = t.$("#v-learn [data-lskip]"); t.click(skip); await sleep(15);
    t.click(t.$("#v-learn [data-lnext]")); await sleep(20);
  }
  ok(t.$("#v-learn").textContent.includes("다시 보고"), "전부 틀림 → 복습 안내");
  let ck = Object.values(t.fake.store.checks || {});
  ok(ck.length === ncon*2 && ck.every(c => c.score === 0 && c.lesson === lid), "checks 컬렉션에 기록");
  ok(!Object.keys(t.fake.store.attempts || {}).length, "문제은행 attempts에는 안 섞임");
  ok(t.fake.store.progress?.[lid] && t.fake.store.progress[lid].done === false, "progress 저장 (미통과)");
  t.click(t.$("#v-learn [data-lgoreview]")); await sleep(10);
  ok(t.w.document.querySelectorAll("#v-learn .sec.review").length === ncon && t.$("#v-learn .banner"), "복습 섹션 강조 + 배너");
  t.click(t.$("#v-learn [data-lretestall]")); await sleep(10);
  // 재시험: 정답으로
  const byId = Object.fromEntries(L.checks.map(c => [c.id, c]));
  const LSx = () => JSON.parse(t.w.localStorage.getItem("oop-learn"));
  for (let i = 0; i < ncon*2; i++){
    const z = LSx().quiz; const q = byId[z.items[z.idx].qid];
    if (q.type === "mc"){ t.click(t.$(`#v-learn [data-lpick="${q.answer}"]`)); await sleep(5); }
    else if (q.type === "ox"){ t.click(t.$(`#v-learn [data-lpick="${q.answer}"]`)); await sleep(5); }
    else { [...t.w.document.querySelectorAll("#v-learn [data-lblank]")].forEach((el, j) => t.type(el, q.accept[j][0])); }
    t.click(t.$("#v-learn [data-lsubmit]")); await sleep(15);
    const pen = t.$("#v-learn .pen")?.textContent; if (pen !== "100") console.log("  not 100:", q.id, pen);
    t.click(t.$("#v-learn [data-lnext]")); await sleep(20);
  }
  ok(t.fake.store.progress[lid].done === true && t.$("#v-learn").textContent.includes("전부 통과"), "재시험 정답 → 레슨 완료");
  ok(LSx().quiz.round === 2, "재시험 회차 기록");
  t.click(t.$('#v-learn [data-topic="copy"]')); await sleep(10);
  ok(!t.$("#v-practice").hidden && t.$("#f-topic")?.value === "copy", "기출 버튼 → 문제 풀기 탭 copy 필터");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  // 4) 모든 점검 문제 정답이 자동 채점에서 100점인지
  t = await boot("ok");
  t.click(t.$('nav.tabs [data-v="learn"]')); await sleep(10);
  let bad = [];
  for (const u of L.units) for (const l of u.lessons){
    t.click(t.$(`#v-learn [data-lesson="${l.id}"]`)); await sleep(5);
    t.click(t.$(`[data-lquiz="${l.id}"]`)); await sleep(5);
    const n = LSx().quiz.items.length;
    for (let i = 0; i < n; i++){
      const z = LSx().quiz; const q = byId[z.items[z.idx].qid];
      if (q.type !== "blank") t.click(t.$(`#v-learn [data-lpick="${q.answer}"]`));
      else [...t.w.document.querySelectorAll("#v-learn [data-lblank]")].forEach((el, j) => t.type(el, q.accept[j][0]));
      await sleep(2); t.click(t.$("#v-learn [data-lsubmit]")); await sleep(8);
      if (t.$("#v-learn .pen")?.textContent !== "100") bad.push(q.id);
      t.click(t.$("#v-learn [data-lnext]")); await sleep(8);
    }
  }
  ok(bad.length === 0, "레슨 23개 점검: 정답 입력 → 전부 100점 " + bad.join(","));
  ok(Object.values(t.fake.store.progress || {}).filter(p => p.done).length === L.units.reduce((s,u)=>s+u.lessons.length,0), "전 레슨 progress done");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  // 5) 노트 한/영 토글
  t = await boot("ok");
  t.click(t.$('nav.tabs [data-v="learn"]')); await sleep(10);
  t.click(t.$('#v-learn [data-lesson="L3-3"]')); await sleep(10);
  const koH = t.$("#s-coupling-cohesion h3").textContent;
  t.click(t.$('#v-learn [data-lang="en"]')); await sleep(10);
  const enH = t.$("#s-coupling-cohesion h3").textContent;
  ok(koH !== enH && !/[가-힣]/.test(t.$("#v-learn .body").textContent) && t.$("#v-learn .body").lang === "en", "English 토글 → 본문 영어 (" + enH + ")");
  ok(!/[가-힣]/.test(t.$("#v-learn .reader h2").textContent), "레슨 제목도 영어");
  ok(JSON.parse(t.w.localStorage.getItem("oop-lang")) === "en", "언어 선택 저장");
  t.click(t.$('#v-learn [data-lang="ko"]')); await sleep(10);
  ok(t.$("#s-coupling-cohesion h3").textContent === koH, "한국어로 복귀");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  console.log(fails ? `\n${fails}개 실패` : "\n전부 통과");
  process.exit(fails ? 1 : 0);
})();
