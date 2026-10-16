# 트레이너 template.html에 학습 탭 한/영 토글을 넣는다 (한 번만 실행). python3 patch_lang.py template.html ca-
import re, sys
path, pfx = sys.argv[1], sys.argv[2]
s = open(path).read()
assert 'data-lang=' not in s, "already patched"
def sub(pat, rep, n=None, regex=False):
    global s
    c = len(re.findall(pat, s)) if regex else s.count(pat)
    assert c and (n is None or c == n), (pat, c)
    s = re.sub(pat, rep, s) if regex else s.replace(pat, rep)
sub('const ls = {', f'let LANG = "ko"; try {{ LANG = JSON.parse(localStorage.getItem("{pfx}lang")) || "ko"; }} catch {{}}\n'
    'const T = (o, k) => (o ? ((LANG === "en" && o[k + "_en"]) || o[k] || "") : "");  // 학습 탭 한/영\nconst ls = {', 1)
sub(r'esc\((l|nx|u|s)\.(title|unitTitle|intro|exam)\)', r'esc(T(\1,"\2"))', regex=True)
sub(r'SEC\[([^\]]+)\]\??\.title', r'T(SEC[\1],"title")', regex=True)
sub('nx.id + " · " + nx.title', 'nx.id + " · " + T(nx,"title")', 1)
sub('§${s.title}', '§${T(s,"title")}', 1)
sub('unitTitle:u.title', 'unitTitle:u.title, unitTitle_en:u.title_en', 1)
sub('let body = l.html;', 'let body = T(l,"html");', 1)
sub('<div class="body">${body}</div>', '<div class="body" lang="${LANG}">${body}</div>', 1)
sub('<aside class="sheet tree" aria-label="단원 목록">',
    '<aside class="sheet tree" aria-label="단원 목록"><div class="langsw" role="group" aria-label="노트 언어"><span class="note">노트</span>'
    '<button class="${LANG==="ko"?"on":""}" data-lang="ko" aria-pressed="${LANG==="ko"}">한국어</button>'
    '<button class="${LANG==="en"?"on":""}" data-lang="en" aria-pressed="${LANG==="en"}">English</button></div>', 1)
sub('  if (ds.home){', f'  if (ds.lang){{ LANG = ds.lang; try {{ localStorage.setItem("{pfx}lang", JSON.stringify(LANG)); }} catch {{}} return view === "learn" ? renderLearn() : renderAll(true); }}\n  if (ds.home){{', 1)
sub('.callout.exam::before{content:"시험 ";font-weight:700;color:var(--warn)}',
    '.callout.exam::before{content:"시험 ";font-weight:700;color:var(--warn)} [lang="en"] .callout.exam::before{content:none}\n'
    '.langsw{display:flex;gap:4px;align-items:center;padding:4px 14px 10px;border-bottom:1px solid var(--line);margin-bottom:4px}'
    '.langsw .note{margin-right:auto}.langsw button{font:inherit;font-size:12px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);background:none;color:var(--muted);cursor:pointer}'
    '.langsw button.on{background:var(--accent);border-color:var(--accent);color:var(--accent-ink,#fff)}', 1)
open(path, 'w').write(s); print("patched", path)
