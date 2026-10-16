// Claude 채점·db 기록·코스 경로 스모크 테스트 (가짜 window.claude 사용)
// node test/smoke_claude.js page.html bank.json
const { JSDOM } = require("jsdom"); const fs = require("fs"); const { install } = require("./fake_claude");
const html = fs.readFileSync(process.argv[2], "utf8"), bankTxt = fs.readFileSync(process.argv[3], "utf8");
const sleep = ms => new Promise(r => setTimeout(r, ms));
let fails = 0; const ok = (c, msg) => { console.log((c ? "PASS " : "FAIL ") + msg); if (!c) fails++; };
const COURSE = { title: "테스트 코스", since: 1, steps: [{ qid: "2025-2", stage: "1단계", goal: "목표" }, { qid: "2025-3", stage: "1단계", goal: "목표2" }] };

async function boot(mode, seed = {}){
  let fake;
  const dom = new JSDOM("<!doctype html><html><body>" + html + "</body></html>", { runScripts: "dangerously", url: "https://x.test/",
    beforeParse(w){ w.scrollTo = () => {}; w.HTMLElement.prototype.scrollIntoView = function(){};
      w.fetch = async () => ({ json: async () => JSON.parse(bankTxt) });
      fake = install(w, { mode, seed }); } });
  const w = dom.window, errs = []; w.addEventListener("error", e => errs.push(e.message));
  const $ = s => w.document.querySelector(s);
  const click = el => { if (!el) throw new Error("missing element"); el.dispatchEvent(new w.MouseEvent("click", { bubbles: true })); };
  const go = qid => { const b = w.document.createElement("button"); b.dataset.go = qid; w.document.body.appendChild(b); click(b); b.remove(); };
  const type = (el, v) => { el.value = v; el.dispatchEvent(new w.Event("input", { bubbles: true })); };
  await sleep(80);
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

  console.log(fails ? `\n${fails}개 실패` : "\n전부 통과");
  process.exit(fails ? 1 : 0);
})();
