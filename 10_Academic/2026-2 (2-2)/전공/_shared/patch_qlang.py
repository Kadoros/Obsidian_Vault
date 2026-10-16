# 문제에도 한/영: python3 patch_qlang.py template.html  (patch_lang.py 다음에 한 번)
import re, sys
path = sys.argv[1]; s = open(path).read()
assert 'class="hlang"' not in s, "already"
def sub(a, b, n=None):
    global s
    c = s.count(a); assert c and (n is None or c == n), (a, c); s = s.replace(a, b)
sub('const T = (o, k) => (o ? ((LANG === "en" && o[k + "_en"]) || o[k] || "") : "");',
    'const T = (o, k) => (!o ? "" : (LANG === "en" && o[k + "_en"] != null) ? o[k + "_en"] : (o[k] ?? ""));', 1)
sub('esc(q.prompt)', 'esc(T(q,"prompt"))')
sub('q.choices.map(', 'T(q,"choices").map(')
sub('q.choices[d]', 'T(q,"choices")[d]')
sub('q.choices[q.answer]', 'T(q,"choices")[q.answer]')
sub('<pre class="code" style="white-space:pre-wrap">${esc(q.answer)}</pre>', '<pre class="code" style="white-space:pre-wrap">${esc(T(q,"answer"))}</pre>')
sub(': q.answer)}</pre>', ': T(q,"answer"))}</pre>')
sub('esc(q.explain)', 'esc(T(q,"explain"))')
sub('Question: ${q.prompt}', 'Question: ${q.prompt}${q.prompt_en ? "\\n(English version) " + q.prompt_en : ""}', 1)
sub('\n${q.answer}\n', '\n${q.answer}${q.answer_en ? "\\n(English version) " + q.answer_en : ""}\n', 1)
sub('q.keys.join(" | ")', 'q.keys.join(" | ") + (q.keys_en ? " || (English) " + q.keys_en.join(" | ") : "")', 1)
# 헤더에 전역 토글 (모든 탭)
m = re.search(r'\n(\s*)<span class="chip" id="store">', s); assert m
sub('<span class="chip" id="store">', '<span class="hlang" role="group" aria-label="언어"><button data-lang="ko">한</button><button data-lang="en">EN</button></span>\n' + m.group(1) + '<span class="chip" id="store">', 1)
sub('.langsw .note{', '.hlang{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}.hlang button{font:inherit;font-family:var(--f-mono,monospace);font-size:11.5px;padding:3px 9px;border:0;background:var(--sheet);color:var(--muted);cursor:pointer}.hlang button.on{background:var(--accent);color:var(--accent-ink,#fff)}\n.langsw .note{', 1)
# 토글 동기화 + 모의고사 중엔 다시 그리지 않음
m = re.search(r'  if \(ds\.lang\)\{ LANG = ds\.lang; (.*?) return (.*?); \}\n', s); assert m, "lang handler"
sub(m.group(0), f'  if (ds.lang){{ LANG = ds.lang; {m.group(1)} syncLang(); if (view === "mock") return; return {m.group(2)}; }}\n', 1)
sub('const T = (o, k) =>', 'function syncLang(){ document.querySelectorAll("[data-lang]").forEach(b => { b.classList.toggle("on", b.dataset.lang === LANG); b.setAttribute("aria-pressed", String(b.dataset.lang === LANG)); }); document.documentElement.lang = LANG; }\nsetTimeout(syncLang, 0);\nconst T = (o, k) =>', 1)
open(path, "w").write(s); print("ok", path)
