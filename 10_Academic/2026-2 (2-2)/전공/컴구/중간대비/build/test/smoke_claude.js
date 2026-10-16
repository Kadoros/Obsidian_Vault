// Claude 채점·db 기록 경로 스모크 테스트 (가짜 window.claude 사용)
// node test/smoke_claude.js ca-trainer.html
const { JSDOM } = require("jsdom"); const fs = require("fs"); const { install } = require("./fake_claude");
const html = fs.readFileSync(process.argv[2], "utf8");
const sleep = ms => new Promise(r => setTimeout(r, ms));
let fails = 0; const ok = (c, msg) => { console.log((c ? "PASS " : "FAIL ") + msg); if (!c) fails++; };

async function boot(mode){
  let fake;
  const dom = new JSDOM("<!doctype html><html><body>" + html + "</body></html>", { runScripts: "dangerously", url: "https://x.test/",
    beforeParse(w){ w.scrollTo = () => {}; w.CSS = { escape: s => s }; w.HTMLElement.prototype.scrollIntoView = function(){};
      fake = install(w, { mode, seed: { extra_questions: { "x-1": { concept: "isa", type: "short", prompt: "EXTRA_Q_MARKER", answer: "a" } } } }); } });
  const w = dom.window, errs = []; w.addEventListener("error", e => errs.push(e.message));
  const $ = s => w.document.querySelector(s), $$ = s => [...w.document.querySelectorAll(s)];
  const click = el => { if (!el) throw new Error("missing element"); el.dispatchEvent(new w.MouseEvent("click", { bubbles: true })); };
  const go = qid => { const b = w.document.createElement("button"); b.dataset.go = qid; w.document.body.appendChild(b); click(b); b.remove(); };
  const type = (el, v) => { el.value = v; el.dispatchEvent(new w.Event("input", { bubbles: true })); };
  await sleep(50);
  return { w, $, $$, click, go, type, errs, fake };
}

(async () => {
  // 1) 정상 채점
  let t = await boot("ok");
  ok(t.$("#grader").textContent.includes("Claude"), "sample 연결 → 채점 칩 'Claude'");
  ok(t.$("#store").textContent.includes("클라우드"), "db 연결 → 저장 칩 '클라우드'");
  t.go("1-ct-1"); await sleep(10);
  t.type(t.$("textarea"), "Cycles_A = 20e9, rate = 4 GHz"); t.click(t.$("[data-psubmit]")); await sleep(50);
  let at = Object.values(t.fake.store.attempts || {});
  ok(at.length === 1 && at[0].grader === "claude" && at[0].score === 0.8 && at[0].mode === "practice", "풀이 문제 Claude 채점 → attempts에 저장");
  ok(t.fake.calls[0]?.opts?.modelTier === "default" && t.fake.calls[0].prompt.includes("Cycles_A = 20e9"), "calc는 default 티어, 학생 답이 프롬프트에 들어감");
  ok(t.$(".pen") && t.$(".fb").textContent.includes("가짜 채점"), "점수·피드백 화면 표시");
  t.click(t.$('[data-self="1"]')); await sleep(20);
  at = Object.values(t.fake.store.attempts);
  ok(at.length === 1 && at[0].grader === "claude+self" && at[0].score === 1, "자가채점 수정 → 같은 기록 update");
  ok(t.w.document.body.textContent.includes("EXTRA_Q_MARKER") || (t.go("x-1"), await sleep(10), t.w.document.body.textContent.includes("EXTRA_Q_MARKER")), "extra_questions 병합");
  // 이해 점검: 서술/풀이는 Claude, 나머지는 자동
  t.click(t.$('nav.tabs [data-v="learn"]')); await sleep(5);
  t.click(t.$('[data-lesson="L1-1"]')); await sleep(5); t.click(t.$("[data-startquiz]")); await sleep(5);
  const D = JSON.parse(t.$("#pl-data").textContent); const Q = Object.fromEntries(D.questions.map(q => [q.id, q]));
  for (let g = 0; g < 12; g++){
    const st = JSON.parse(t.w.localStorage.getItem("ca-learn")); if (st.mode !== "quiz") break;
    const q = Q[st.quiz.items[st.quiz.idx].qid] || { type: "short" };
    if (q.type === "mc" || q.type === "ox"){ t.click(t.$(`[data-pick="${q.answer}"]`)); t.click(t.$("[data-submit]")); }
    else if (q.type === "blank"){ t.$$("[data-blank]").forEach((i, k) => i.value = q.accept[k][0]); t.click(t.$("[data-submit]")); }
    else { t.type(t.$("textarea"), "답안"); t.click(t.$("[data-submit]")); }
    await sleep(40); t.click(t.$("[data-qnext]")); await sleep(20);
  }
  at = Object.values(t.fake.store.attempts);
  ok(at.some(a => a.mode === "check"), "점검 퀴즈 기록 저장 (mode check)");
  ok(!!t.fake.store.progress?.["L1-1"], "progress/L1-1 문서 저장");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  // 2) 채점 실패(rate_limited) → 에러 안내 + 자가채점 폴백
  t = await boot("rate_limited");
  t.go("1-ct-1"); await sleep(10);
  t.type(t.$("textarea"), "아무 답"); t.click(t.$("[data-psubmit]")); await sleep(50);
  ok(t.$(".result .err")?.textContent.includes("몰렸어"), "rate_limited 안내 문구");
  ok(!Object.keys(t.fake.store.attempts || {}).length, "실패한 채점은 기록 안 함");
  t.click(t.$('[data-self="0.5"]')); await sleep(20);
  at = Object.values(t.fake.store.attempts || {});
  ok(at.length === 1 && at[0].grader === "self" && at[0].score === 0.5, "자가채점 폴백 기록");
  ok(t.errs.length === 0, "JS 에러 없음 " + JSON.stringify(t.errs));

  console.log(fails ? `\n${fails}개 실패` : "\n전부 통과");
  process.exit(fails ? 1 : 0);
})();
