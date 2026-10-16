// 수업 따라가기 · 놀이터 · 제어신호(sig) 채점 · 모의고사 구성 스모크 테스트
// node test/smoke_walk.js ca-trainer.html
const { JSDOM } = require("jsdom"); const fs = require("fs");
const html = fs.readFileSync(process.argv[2], "utf8");
const sleep = ms => new Promise(r => setTimeout(r, ms));
let fails = 0; const ok = (c, msg) => { console.log((c ? "PASS " : "FAIL ") + msg); if (!c) fails++; };
const dom = new JSDOM("<!doctype html><html><body>" + html + "</body></html>", { runScripts: "dangerously", url: "https://x.test/",
  beforeParse(w){ w.scrollTo = () => {}; w.CSS = { escape: s => s }; w.HTMLElement.prototype.scrollIntoView = function(){}; } });
const w = dom.window, errs = []; w.addEventListener("error", e => errs.push(e.message));
const $ = s => w.document.querySelector(s), $$ = s => [...w.document.querySelectorAll(s)];
const click = el => { if (!el) throw new Error("missing element"); el.dispatchEvent(new w.MouseEvent("click", { bubbles: true })); };
const key = k => w.document.dispatchEvent(new w.KeyboardEvent("keydown", { key: k, bubbles: true }));
(async () => {
  await sleep(40);
  const D = JSON.parse($("#pl-data").textContent);
  // 1) 수업 따라가기
  click($('nav.tabs [data-v="walk"]')); await sleep(5);
  ok($$(".wtab").length === 3, "수업 탭 3개 (6주-1, 6주-2, 놀이터)");
  click($('[data-wlec="w6-2"]')); await sleep(5);
  ok($$(".wrow").length === D.walk.lectures[1].steps.length, "6주-2 장면 목록 " + $$(".wrow").length);
  click($('[data-wstep="6"]')); await sleep(5);
  ok(!!$(".stage img") && $(".stage img").getAttribute("src") === "img/w6-p03.jpg", "MUX 장면 → p.3 이미지");
  ok(!!$(".stage svg mask") && $$(".stage .focus").length >= 2, "블라인드 마스크 + 포커스 박스");
  ok($$(".stage .flow").length >= 1 && $$(".wmark").length >= 2, "신호 경로 + 마크");
  key("ArrowRight"); await sleep(5);
  ok(JSON.parse(w.localStorage.getItem("ca-walk")).idx === 7, "→ 키로 다음 장면");
  click($("[data-wblind]")); await sleep(5);
  ok(!$(".stage svg mask"), "가림 끄기 → 마스크 없음");
  click($("[data-wblind]")); await sleep(5);
  click($('[data-wstep="0"]')); await sleep(5);
  ok(!!$(".nocard"), "슬라이드 없는 공지 장면은 카드로");
  // 모든 장면 렌더 오류 없나
  for (const lec of D.walk.lectures){ click($(`[data-wlec="${lec.id}"]`)); await sleep(2);
    for (let i = 0; i < lec.steps.length; i++){ click($(`[data-wstep="${i}"]`)); await sleep(1); } }
  ok(errs.length === 0, "80개 장면 모두 렌더 (에러 없음)");
  // 2) 놀이터
  click($('[data-wlec="play"]')); await sleep(5);
  for (const id of ["add","lw","sw","beq"]){ click($(`[data-winst="${id}"]`)); await sleep(3); }
  ok($$(".sigrow").length === 9 && $(".sigrow b.vX"), "놀이터 beq: 신호 9개, X 표시");
  // 3) sig 문제 채점
  const q = D.questions.find(x => x.id === "4-rt-1");
  const b = w.document.createElement("button"); b.dataset.go = "4-rt-1"; w.document.body.appendChild(b); click(b); b.remove(); await sleep(5);
  for (const [k, v] of Object.entries(q.sig)) click($(`[data-sigk="${k}"][data-sigv="${v}"]`));
  click($("[data-psubmit]")); await sleep(10);
  let at = JSON.parse(w.localStorage.getItem("ca-attempts") || "[]");
  ok(at.length === 1 && at[0].score === 1 && at[0].grader === "auto", "sig 전부 정답 → 100점 자동 채점");
  click($("[data-pretry]")); await sleep(5);
  for (const [k, v] of Object.entries(q.sig)) click($(`[data-sigk="${k}"][data-sigv="${k === "RegDst" ? "0" : v}"]`));
  click($("[data-psubmit]")); await sleep(10);
  at = JSON.parse(w.localStorage.getItem("ca-attempts") || "[]");
  ok(at.length === 2 && Math.abs(at[1].score - 8/9) < 1e-9 && $$(".missed li").length === 1, "RegDst 하나 틀림 → 8/9, 틀린 신호 표시");
  // 4) 모의고사
  click($('nav.tabs [data-v="mock"]')); await sleep(5);
  click($("[data-mockstart]")); await sleep(5);
  ok($$(".mockq").length === D.mock.slots.length, "모의고사 " + $$(".mockq").length + "문항");
  ok($(".mockhead .label").textContent.includes("100점"), "총 100점");
  // 5) 레슨 → 수업 장면 링크
  click($('nav.tabs [data-v="learn"]')); await sleep(5);
  click($('[data-lesson="L1-1"]')); await sleep(5);
  ok($$(".sec").length > 0, "레슨 읽기 화면");
  const lessonWithWalk = D.units[3].lessons[3].id;
  const st = JSON.parse(w.localStorage.getItem("ca-learn")); st.lesson = lessonWithWalk; st.mode = "read";
  ok(D.units[3].lessons[3].html.includes('data-walk="'), "U4 레슨에 수업 장면 버튼 포함");
  ok(errs.length === 0, "JS 에러 없음 " + JSON.stringify(errs));
  console.log(fails ? `\n${fails}개 실패` : "\n전부 통과"); process.exit(fails ? 1 : 0);
})();
