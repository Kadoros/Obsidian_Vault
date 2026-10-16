# lessons*.md + checks*.py → ../../learn.json  (python3 build_learn.py)
import re, json, html, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,'.')
import cdsl, checks1, checks2
from figs import FIGS
PROF = {}
def inline(s):
    s=html.escape(s, quote=False)
    s=re.sub(r'`([^`]+)`', lambda m:'<code>'+m.group(1)+'</code>', s)
    s=re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

def md2html(lines):
    out=[]; i=0; n=len(lines)
    def is_li(l): return re.match(r'^\s*(- |\d+\. )', l)
    while i<n:
        l=lines[i]
        if not l.strip(): i+=1; continue
        if l.startswith('```'):
            j=i+1; buf=[]
            while j<n and not lines[j].startswith('```'): buf.append(lines[j]); j+=1
            out.append('<pre class="code">'+html.escape('\n'.join(buf))+'</pre>'); i=j+1; continue
        if l.startswith('|'):
            rows=[]
            while i<n and lines[i].startswith('|'): rows.append(lines[i]); i+=1
            cells=[ [c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            head=cells[0]; body=[c for c in cells[2:]]
            t='<div class="tblw"><table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in head)+'</tr></thead><tbody>'
            t+=''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in body)+'</tbody></table></div>'
            out.append(t); continue
        if l.startswith('>'):
            buf=[]
            while i<n and lines[i].startswith('>'): buf.append(lines[i][1:].strip()); i+=1
            txt=' '.join(buf)
            cls='callout exam' if '시험' in txt[:12] else ('callout trap' if re.match(r'(함정|실수|주의)',txt) else 'callout')
            out.append(f'<div class="{cls}">{inline(txt)}</div>'); continue
        if is_li(l):
            ordered=bool(re.match(r'^\s*\d+\. ',l))
            items=[]
            while i<n and lines[i].strip() and (is_li(lines[i]) or lines[i].startswith('  ')):
                m=re.match(r'^(\s*)(- |\d+\. )(.*)$', lines[i])
                if m and len(m.group(1))==0:
                    items.append([m.group(3)])
                else:
                    items[-1].append(lines[i].strip())
                i+=1
            tag='ol' if ordered else 'ul'
            h=f'<{tag}>'
            for it in items:
                sub=[s for s in it[1:]]
                h+='<li>'+inline(it[0])
                if sub:
                    subs=[re.sub(r'^(- |\d+\. )','',s) for s in sub]
                    if all(re.match(r'^(- |\d+\. )',s) for s in sub):
                        h+='<ul>'+''.join('<li>'+inline(s)+'</li>' for s in subs)+'</ul>'
                    else:
                        h+='<div class="sub">'+'<br>'.join(inline(s) for s in sub)+'</div>'
                h+='</li>'
            out.append(h+f'</{tag}>'); continue
        buf=[]
        while i<n and lines[i].strip() and not lines[i].startswith(('```','|','>','## ')) and not is_li(lines[i]):
            buf.append(lines[i]); i+=1
        out.append('<p>'+'<br>'.join(inline(b) for b in buf)+'</p>')
    return '\n'.join(out)

# 개념 → 문제은행(bank.json) topic: '관련 기출' 버튼이 문제 풀기 탭의 주제 필터로 감
T = {}
for t, cs in {
 "se":"crisis lifecycle se-def sw-props maintenance",
 "quality":"quality robust",
 "paradigm":"unstructured procedural global-vars oop-why",
 "encap":"adt class-object encap-intro interface-impl public-private abs-encap two-views encap-benefits method message-passing avoid-public getter-setter visibility",
 "inherit":"inherit-poly",
 "trace":"cpp-io cpp-basics obj-pointer separate-def",
 "memory":"pointer new-delete static-dynamic object-creation leak-dangling memory-safe",
 "ctor":"class-basic constructor default-ctor",
 "fileio":"fstream open-modes seek-tell binary",
 "design":"rdd dev-process scenario component crc iikh-components behavior-state naming implement stub",
 "couple":"coupling-cohesion",
 "assert":"assert", "copy":"copy-when shallow-deep rule-of-three cow", "static":"static-member",
 "constfn":"const-fn", "inline":"inline", "friend":"friend",
 "passing":"reference ref-vs-pointer pass-modes pass-guide return-local", "stack":"tintstack",
 "opover":"opover-basic opover-complex"}.items():
  for c in cs.split(): T[c] = t
units=[]; cur=None; les=None
text=''.join(open(f'lessons{k}.md').read()+'\n' for k in range(1,6))
for raw in text.split('\n'):
    if raw.startswith('@unit '):
        uid,title,src=[x.strip() for x in raw[6:].split('|')]
        cur={"id":uid,"title":title,"src":src,"intro":"","lessons":[]}; units.append(cur); les=None; continue
    if raw.startswith('@intro '): cur["intro"]=raw[7:].strip(); continue
    if raw.startswith('@lesson '):
        lid,title,src=[x.strip() for x in raw[8:].split('|')]
        les={"id":lid,"title":title,"src":src,"secs":[],"_lines":[]}; cur["lessons"].append(les); continue
    if les is not None: les["_lines"].append(raw)

sec_of={}
for u in units:
    for l in u["lessons"]:
        # split by ## headings
        chunks=[]; curc=None
        for line in l["_lines"]:
            m=re.match(r'^## (.+?)\s*\{#([\w-]+)\}\s*$', line)
            if m:
                curc={"id":m.group(2),"title":m.group(1),"lines":[]}; chunks.append(curc)
            elif curc is not None: curc["lines"].append(line)
        l["md"]='\n'.join(l["_lines"]).strip()
        hs=[]
        for c in chunks:
            assert c["id"] not in sec_of, c["id"]
            sec_of[c["id"]]=(u["id"],l["id"],c["title"])
            l["secs"].append({"id":c["id"],"title":c["title"]})
            figs=''.join(f'<figure class="slide"><button class="zoom" data-zoom="img/{f}.jpg" aria-label="크게 보기"><img src="img/{f}.jpg" alt="{html.escape(cap)}" loading="lazy"></button><figcaption>{html.escape(cap)}</figcaption></figure>' for f,cap in FIGS.get(c["id"],[]))
            pn=PROF.get(c['id']); prof=f'<div class="callout prof"><b>수업 메모</b> <span class="src">{html.escape(pn[0])}</span><br>{inline(pn[1])}</div>' if pn else ''
            hs.append(f'<section class="sec" id="s-{c["id"]}"><h3>{inline(c["title"])}</h3>{md2html(c["lines"])}{prof}{figs}</section>')
            for f,cap in FIGS.get(c["id"],[]): c["lines"].append(f"\n![[img/{f}.jpg]]\n*{cap}*")
        l["html"]='\n'.join(hs); del l["_lines"]

qs = cdsl.CS; ids = set()
for q in qs:
    assert q["id"] not in ids, q["id"]; ids.add(q["id"])
    assert q["concept"] in sec_of, (q["id"], q["concept"])
    q["lesson"] = sec_of[q["concept"]][1]
from collections import Counter
cc = Counter(q["concept"] for q in qs)
missing = [s for s in sec_of if s not in cc]; assert not missing, ("sections without checks", missing)
assert set(T) == set(sec_of), (set(sec_of) - set(T), set(T) - set(sec_of))
for u in units:
    for l in u["lessons"]:
        l["topics"] = sorted({T[s["id"]] for s in l["secs"]})
        for s in l["secs"]: s["topic"] = T[s["id"]]
        del l["md"]
print("units", len(units), "lessons", sum(len(u["lessons"]) for u in units), "sections", len(sec_of), "checks", len(qs), Counter(q["type"] for q in qs))
print("1-check concepts:", [c for c, v in cc.items() if v == 1])
json.dump({"version":1, "units":units, "checks":qs}, open("../../learn.json","w"), ensure_ascii=False)
print("learn.json bytes", os.path.getsize("../../learn.json"))
