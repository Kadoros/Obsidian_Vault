import json, re, html, sys
B = "/home/user/Obsidian_Vault/10_Academic/2026-2 (2-2)/전공/"
S = sys.argv[1]
SUBJ = [  # (key, 제목, data, img dir, 출력)
 ("pl", "프로그래밍 언어론 · 중간 학습 노트", B+"프밍언/중간대비/build/data.json", B+"프밍언/중간대비/img", B+"프밍언/중간대비/프밍언 학습 노트.pdf"),
 ("ca", "컴퓨터 구조 · 중간 학습 노트", S+"/cg/data.json", B+"컴구/중간대비/img", B+"컴구/중간대비/컴구 학습 노트.pdf"),
 ("db", "데이터베이스 · 중간 학습 노트", B+"DB/중간대비/build/data.json", B+"DB/중간대비/img", B+"DB/중간대비/DB 학습 노트.pdf"),
 ("oop", "객체지향 프로그래밍 · 중간 학습 노트", B+"객체프/중간대비/learn.json", B+"객체프/중간대비/img", B+"객체프/중간대비/객체프 학습 노트.pdf"),
]
CSS = open(S+"/note.css").read()
jobs = []
for key, title, dp, img, out in SUBJ:
    d = json.load(open(dp)); units = d["units"]
    nl = sum(len(u["lessons"]) for u in units)
    toc = "".join(f'<div class="tu"><b>{html.escape(u["id"])}</b> {html.escape(u["title"])}</div>' +
        "".join(f'<div class="tl"><a href="#l-{l["id"]}">{html.escape(l["id"])} · {html.escape(l["title"])}</a></div>' for l in u["lessons"]) for u in units)
    body = []
    for u in units:
        body.append(f'<section class="unit"><div class="uid">{html.escape(u["id"])} · {html.escape(u.get("src",""))}</div><h1>{html.escape(u["title"])}</h1>' + (f'<p class="intro">{html.escape(u.get("intro",""))}</p>' if u.get("intro") else "") + '</section>')
        for l in u["lessons"]:
            h = l["html"]
            h = re.sub(r'<div class="actions"[^>]*>.*?</div>', '', h, flags=re.S)
            h = re.sub(r'<button class="zoom"[^>]*>(.*?)</button>', r'\1', h, flags=re.S)
            h = re.sub(r'<button[^>]*>.*?</button>', '', h, flags=re.S)
            h = h.replace('src="img/', f'src="file://{img}/').replace(' loading="lazy"', '')
            body.append(f'<article class="lesson" id="l-{l["id"]}"><div class="lid">{html.escape(l["id"])} · {html.escape(u["title"])}</div><h2>{html.escape(l["title"])}</h2><div class="lsrc">교안 범위: {html.escape(l.get("src",""))}</div>{h}</article>')
    doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>' \
      f'<section class="cover"><div class="k">2026-2 중간고사 대비</div><h1>{html.escape(title)}</h1><div class="m">단원 {len(units)}개 · 레슨 {nl}개 · 트레이너 학습 탭과 같은 내용</div><div class="toc">{toc}</div></section>' + "".join(body) + '</body></html>'
    hp = f"{S}/{key}.html"; open(hp, "w").write(doc); jobs.append((hp, out, title))
json.dump(jobs, open(S+"/jobs.json", "w"), ensure_ascii=False)
print(len(jobs))
