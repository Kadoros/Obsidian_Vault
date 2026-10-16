import re, json, html, sys, importlib
from collections import Counter
sys.path.insert(0, '.')
import qdsl
from figs import FIGS
from prof import PROF
import meta, walk
for m in ["q1", "q2", "q3", "q4", "q5"]: importlib.import_module(m)

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', lambda m: '<code>' + m.group(1) + '</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

def md2html(lines):
    out = []; i = 0; n = len(lines)
    def is_li(l): return re.match(r'^\s*(- |\d+\. )', l)
    while i < n:
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith('```'):
            j = i + 1; buf = []
            while j < n and not lines[j].startswith('```'): buf.append(lines[j]); j += 1
            out.append('<pre class="code">' + html.escape('\n'.join(buf)) + '</pre>'); i = j + 1; continue
        if l.startswith('|'):
            rows = []
            while i < n and lines[i].startswith('|'): rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            head = cells[0]; body = cells[2:]
            t = '<div class="tblw"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>'
            t += ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body) + '</tbody></table></div>'
            out.append(t); continue
        if l.startswith('>'):
            buf = []
            while i < n and lines[i].startswith('>'): buf.append(lines[i][1:].strip()); i += 1
            txt = ' '.join(buf)
            cls = 'callout exam' if txt.startswith(('시험','Exam')) else ('callout trap' if re.match(r'(함정|실수|주의|Trap|Caution|Pitfall|Mistake)', txt) else 'callout')
            out.append(f'<div class="{cls}">{inline(txt)}</div>'); continue
        if is_li(l):
            ordered = bool(re.match(r'^\s*\d+\. ', l)); items = []
            while i < n and lines[i].strip() and (is_li(lines[i]) or lines[i].startswith('  ')):
                m = re.match(r'^(\s*)(- |\d+\. )(.*)$', lines[i])
                if m and len(m.group(1)) == 0: items.append([m.group(3)])
                else: items[-1].append(lines[i].strip())
                i += 1
            tag = 'ol' if ordered else 'ul'; h = f'<{tag}>'
            for it in items:
                sub = it[1:]; h += '<li>' + inline(it[0])
                if sub:
                    subs = [re.sub(r'^(- |\d+\. )', '', s) for s in sub]
                    if all(re.match(r'^(- |\d+\. )', s) for s in sub): h += '<ul>' + ''.join('<li>' + inline(s) + '</li>' for s in subs) + '</ul>'
                    else: h += '<div class="sub">' + '<br>'.join(inline(s) for s in sub) + '</div>'
                h += '</li>'
            out.append(h + f'</{tag}>'); continue
        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith(('```', '|', '>', '## ')) and not is_li(lines[i]):
            buf.append(lines[i]); i += 1
        out.append('<p>' + '<br>'.join(inline(b) for b in buf) + '</p>')
    return '\n'.join(out)

# ── 수업 따라가기 데이터 + 개념 → 장면 링크 ──
WALK = walk.build()
WLINK = {}
for lec in WALK["lectures"]:
    for i, st in enumerate(lec["steps"]):
        WLINK.setdefault(st["concept"], []).append((lec["id"], i, lec["title"].split(" ")[0], st["t"], st["h"]))

units = []; cur = None; les = None
text = ''.join(open(f'lessons{k}.md').read() + '\n' for k in range(1, 5))
for raw in text.split('\n'):
    if raw.startswith('@unit '):
        uid, title, src = [x.strip() for x in raw[6:].split('|')]
        cur = {"id": uid, "title": title, "src": src, "intro": "", "lessons": []}; units.append(cur); les = None; continue
    if raw.startswith('@intro '): cur["intro"] = raw[7:].strip(); continue
    if raw.startswith('@lesson '):
        parts = [x.strip() for x in raw[8:].split('|')]
        lid, title, src = parts[:3]
        les = {"id": lid, "title": title, "src": src, "exam": parts[3] if len(parts) > 3 else "", "secs": [], "_lines": []}
        cur["lessons"].append(les); continue
    if les is not None: les["_lines"].append(raw)

sec_of = {}; MD = []
for u in units:
    MD.append(f"## {u['id']} {u['title']}\n*{u['src']}*\n\n{u['intro']}\n")
    for l in u["lessons"]:
        chunks = []; curc = None
        for line in l["_lines"]:
            m = re.match(r'^## (.+?)\s*\{#([\w-]+)\}\s*$', line)
            if m: curc = {"id": m.group(2), "title": m.group(1), "lines": []}; chunks.append(curc)
            elif curc is not None: curc["lines"].append(line)
        l["md"] = '\n'.join(l["_lines"]).strip()
        MD.append(f"### {l['id']} {l['title']}\n*교안: {l['src']}*\n")
        hs = []
        for c in chunks:
            assert c["id"] not in sec_of, c["id"]
            sec_of[c["id"]] = (u["id"], l["id"], c["title"])
            l["secs"].append({"id": c["id"], "title": c["title"]})
            figs = ''.join(f'<figure class="slide"><button class="zoom" data-zoom="img/{f}.jpg" aria-label="크게 보기"><img src="img/{f}.jpg" alt="{html.escape(cap)}" loading="lazy"></button><figcaption>{html.escape(cap)}</figcaption></figure>' for f, cap in FIGS.get(c["id"], []))
            pn = PROF.get(c['id'])
            prof = f'<div class="callout prof"><b>수업 메모</b> <span class="src">{html.escape(pn[0])}</span><br>{inline(pn[1])}</div>' if pn else ''
            wl = WLINK.get(c["id"], [])[:6]
            walks = ('<div class="actions" style="margin:4px 0 10px">' + ''.join(
                f'<button class="btn sm ghost" data-walk="{lid}:{i}">▶ {html.escape(t)} {html.escape(ts)} {html.escape(h)}</button>' for lid, i, t, ts, h in wl) + '</div>') if wl else ''
            hs.append(f'<section class="sec" id="s-{c["id"]}"><h3>{inline(c["title"])}</h3>{md2html(c["lines"])}{prof}{walks}{figs}</section>')
            body = '\n'.join(c["lines"]).strip()
            body = re.sub(r'^> (시험[^\n]*)', r'> [!warning] \1', body, flags=re.M)
            MD.append(f"#### {c['title']}\n\n{body}\n")
            if pn: MD.append(f"> [!note] 수업 메모 ({pn[0]})\n> {pn[1]}\n")
            if wl: MD.append("> [!example] 수업 장면: " + " · ".join(f"{t} {ts} {h}" for _, _, t, ts, h in wl) + "\n")
            for f, cap in FIGS.get(c["id"], []): MD.append(f"![[img/{f}.jpg]]\n*{cap}*\n")
        l["html"] = '\n'.join(hs); del l["_lines"]

# 영어판 (lessonsN.en.md, figs_en.py, prof_en.py) → html_en·title_en
import os as _os
if _os.path.exists('lessons1.en.md'):
    sys.path.insert(0, '../../../_shared'); from en_lessons import attach_en; from figs_en import CAP_EN
    try: from prof_en import PROF_EN
    except ImportError: PROF_EN = {}
    attach_en(units, [f'lessons{k}.en.md' for k in range(1, 5)], md2html, inline, FIGS, CAP_EN, PROF_EN)
    print("english: ok")

qs = qdsl.QS; ids = set()
for q in qs:
    assert q["id"] not in ids, q["id"]; ids.add(q["id"])
    assert q["concept"] in sec_of, (q["id"], q["concept"])
    q["lesson"] = sec_of[q["concept"]][1]; q["unit"] = sec_of[q["concept"]][0]
    if q["type"] == "mc": assert 0 <= q["answer"] < len(q["choices"]), q["id"]
    if q["type"] == "blank": assert q["prompt"].count("(") >= len(q["accept"]), q["id"]
    if q["type"] == "sig": assert all(v in ("0", "1", "X") for v in q["sig"].values()), q["id"]
    if q.get("slot"): assert q["slot"] in {s["slot"] for s in meta.MOCK["slots"]}, q["id"]
for st in (s for l in WALK["lectures"] for s in l["steps"]):
    assert st["concept"] in sec_of, ("walk", st["t"], st["concept"])
for c in meta.WEIGHTS: assert c in sec_of, ("weight", c)

cc = Counter(q["concept"] for q in qs)
W = {c: meta.WEIGHTS.get(c, 2) for c in sec_of}
print("questions:", len(qs), " lessons:", sum(len(u["lessons"]) for u in units), " sections:", len(sec_of))
print("sections without questions:", [s for s in sec_of if s not in cc])
print("by type:", Counter(q["type"] for q in qs))
print("slots:", sorted(Counter(q.get("slot") for q in qs if q.get("slot")).items()))
print("below weight+1:", [(c, W[c], cc[c]) for c in sec_of if cc[c] < W[c] + 1])
print("walk steps:", [(l["id"], len(l["steps"])) for l in WALK["lectures"]])

# 문제 영어판 (q_en*.json)
import glob as _glob
if _glob.glob('q_en*.json'):
    sys.path.insert(0, '../../../_shared'); from en_lessons import attach_q_en
    print("english questions:", attach_q_en(qs, sorted(_glob.glob('q_en*.json'))))

data = {"units": units, "questions": qs, "weights": W, "walk": WALK, "mock": meta.MOCK,
        "examNotes": meta.EXAM_NOTES, "homeNotes": meta.HOME_NOTES}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
json.dump({"version": 1, "questions": qs}, open('bank.json', 'w'), ensure_ascii=False, indent=1)
open('정리.md', 'w').write("# 컴구 중간 정리\n\n> 교안 week1–6 + 수업 전사 기반. 트레이너 artifact의 레슨 본문과 같은 내용. '수업 메모'는 녹음 전사에서 뽑은 교수님 설명.\n\n" + '\n'.join(MD))
print("data.json bytes", len(json.dumps(data, ensure_ascii=False).encode()))
