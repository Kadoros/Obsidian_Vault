/* ── 기록 백업: 내보내기(.json) / 가져오기 ─────────── 클라우드·이 브라우저 기록을 파일로 옮긴다 (Claude 앱 ↔ 로컬 html). */
function bkKey(a){ return a._id && a._id !== "local" ? a._id : a.at + "|" + a.qid; }
function bkData(){
  const out = { app:BK_PFX, name:BK_NAME, at:Date.now(), attempts:attempts.map(a => ({ ...a })), progress:{ ...progress } };
  if (typeof checks !== "undefined") out.checks = checks.map(a => ({ ...a }));
  return out;
}
function bkMsg(t, bad){ const el = document.getElementById("bk-msg"); if (el){ el.textContent = t; el.style.color = bad ? "var(--bad)" : ""; } }
async function bkExport(){
  const d = bkData(), txt = JSON.stringify(d);
  const name = `${BK_PFX}backup-${new Date().toISOString().slice(0,10)}.json`;  // 한글 파일명은 브라우저가 버리는 경우가 있어서 ASCII
  const n = `문항 기록 ${d.attempts.length}개 · 레슨 ${Object.keys(d.progress).length}개${d.checks ? ` · 점검 ${d.checks.length}개` : ""}`;
  const dl = window.claude?.use ? await claude.use("downloads").catch(() => null) : null;
  if (dl){
    try { await dl.save({ filename:name, data:txt }); return bkMsg("저장했어 (" + n + ")."); }
    catch(e){ if (e?.code === "declined") return bkMsg("저장을 취소했어."); if (e?.code === "rate_limited") return bkMsg("저장 창이 이미 열려 있어.", true); }
  }
  try {
    const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([txt], { type:"application/json" })); a.download = name;
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    bkMsg("다운로드했어 (" + n + ").");
  } catch { bkMsg("이 화면에선 파일 저장이 안 돼.", true); }
}
async function bkMergeList(name, incoming, cur){
  const have = new Set(cur.map(bkKey)); const add = incoming.filter(a => a && a.qid && !have.has(bkKey(a)));
  let cloud = 0;
  for (const a of add){
    const id = a._id && a._id !== "local" ? a._id : (a.at || Date.now()) + "-" + Math.random().toString(36).slice(2,8);
    const { _id, ...doc } = a;
    if (db){ try { await db.collection(name).doc(id).set(doc); cloud++; cur.push({ ...doc, _id:id }); continue; } catch {} }
    const loc = ls.get(BK_PFX + name, []); loc.push({ ...doc, _id:id }); ls.set(BK_PFX + name, loc); cur.push({ ...doc, _id:id });
  }
  return add.length;
}
async function bkImport(file){
  let d; try { d = JSON.parse(await file.text()); } catch { return bkMsg("JSON 파일이 아니야.", true); }
  if (d.app !== BK_PFX) return bkMsg(`다른 과목 기록이야 (${d.name || d.app || "?"}). ${BK_NAME} 기록 파일을 골라줘.`, true);
  bkMsg("가져오는 중…");
  const na = await bkMergeList("attempts", d.attempts || [], attempts);
  let nc = 0; if (typeof checks !== "undefined" && d.checks) nc = await bkMergeList("checks", d.checks, checks);
  let np = 0; const lp = ls.get(BK_PFX + "progress", {});
  for (const [lid, p] of Object.entries(d.progress || {})){
    const cur = progress[lid] || {};
    if (!p || (cur.done && !p.done)) continue;
    const merged = { ...cur, ...p, passed:{ ...(cur.passed || {}), ...(p.passed || {}) }, done:!!(cur.done || p.done) };
    if (JSON.stringify(merged) === JSON.stringify(cur)) continue;
    progress[lid] = merged; lp[lid] = merged; np++;
    if (db){ try { await db.collection("progress").doc(lid).set(merged); } catch {} }
  }
  ls.set(BK_PFX + "progress", lp);
  renderAll(true);
  bkMsg(`가져왔어: 새 문항 기록 ${na}개 · 레슨 진행 ${np}개${nc ? ` · 점검 ${nc}개` : ""}${db ? " (클라우드에도 저장)" : " (이 브라우저에 저장)"}.`);
}
function bkPanel(){
  return `<div class="sheet" id="bk" style="padding:12px 14px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center">
    <b style="margin-right:4px">기록 백업</b>
    <button class="btn sm" data-bkexp="1">기록 내보내기 (.json)</button>
    <label class="btn sm" style="cursor:pointer">기록 가져오기<input type="file" accept=".json,application/json" data-bkimp="1" hidden></label>
    <span class="note" id="bk-msg">Claude 앱 ↔ 볼트의 html 파일 사이에 기록을 옮길 때. 가져오기는 합치기라 기존 기록은 안 지워져.</span></div>`;
}
{ const _rh = renderHist; renderHist = function(...a){ const r = _rh.apply(this, a); const v = document.getElementById("v-hist"); if (v && !v.querySelector("#bk")) v.insertAdjacentHTML("afterbegin", bkPanel()); return r; }; }
document.addEventListener("click", e => { if (e.target.closest?.("[data-bkexp]")) bkExport(); });
document.addEventListener("change", e => { if (e.target.matches?.("[data-bkimp]") && e.target.files[0]){ bkImport(e.target.files[0]); e.target.value = ""; } });
