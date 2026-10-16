// jsdom용 가짜 window.claude: sample(채점)·db(기록)를 흉내 내서 Claude 채점 경로를 오프라인으로 검증한다.
// mode: "ok" = 채점 성공, "rate_limited" / "not_granted" = sample.json이 그 코드로 실패
function install(win, { mode = "ok", seed = {} } = {}){
  const store = {};            // collection -> {id: doc}
  const subs = {};             // collection -> [listener]
  const calls = [];            // sample.json 호출 기록
  const col = name => (store[name] ||= {});
  for (const [c, docs] of Object.entries(seed)) Object.assign(col(c), docs);
  const snap = name => ({ docs: Object.entries(col(name)).map(([id, d]) => ({ id, data: () => ({ ...d }) })) });
  const fire = name => (subs[name] || []).forEach(f => f(snap(name)));
  const collection = name => {
    const q = {
      orderBy(){ return q; }, limit(){ return q; },
      onSnapshot(cb){ (subs[name] ||= []).push(cb); setTimeout(() => cb(snap(name)), 0); return () => {}; },
      doc(id){ return {
        async set(d){ col(name)[id] = { ...d }; fire(name); },
        async update(p){ if (!col(name)[id]) { const e = new Error("not found"); e.code = "not_found"; throw e; } Object.assign(col(name)[id], p); fire(name); },
      }; },
    };
    return q;
  };
  const db = {
    collection,
    doc(path){ const [c, id] = path.split("/");
      return { onSnapshot(cb){ setTimeout(() => { const d = col(c)[id]; cb({ exists: !!d, data: () => d }); }, 0); return () => {}; } }; },
  };
  const sample = {
    async json(prompt, opts){
      calls.push({ prompt, opts });
      if (mode !== "ok"){ const e = new Error(mode); e.code = mode; throw e; }
      return { score: 0.8, verdict: "partial", feedback: "가짜 채점 피드백", missed: ["빠진 항목"], english: "" };
    },
  };
  win.claude = { use: async name => {
    if (name === "sample") return sample;
    if (name === "db") return db;
    if (name === "user") return { id: "u1", name: "test" };
    const e = new Error("not_granted"); e.code = "not_granted"; throw e;
  } };
  return { store, calls };
}
module.exports = { install };
