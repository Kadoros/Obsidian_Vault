"""영어판 레슨: lessonsN.en.md를 한국어판과 같은 구조로 읽어서 units에 *_en 필드를 붙인다.
attach_en(units, paths, md2html, inline, figs, cap_en, prof_en) — 레슨·섹션 id가 한국어판과 다르면 assert."""
import re, html

def parse(paths):
    units = []; cur = les = None
    for raw in ''.join(open(p).read() + '\n' for p in paths).split('\n'):
        if raw.startswith('@unit '):
            uid, title, src = [x.strip() for x in raw[6:].split('|')][:3]
            cur = {"id": uid, "title": title, "intro": "", "lessons": []}; units.append(cur); les = None; continue
        if raw.startswith('@intro '): cur["intro"] = raw[7:].strip(); continue
        if raw.startswith('@lesson '):
            parts = [x.strip() for x in raw[8:].split('|')]
            les = {"id": parts[0], "title": parts[1], "exam": parts[3] if len(parts) > 3 else "", "_lines": []}
            cur["lessons"].append(les); continue
        if les is not None: les["_lines"].append(raw)
    for u in units:
        for l in u["lessons"]:
            chunks = []; c = None
            for line in l.pop("_lines"):
                m = re.match(r'^## (.+?)\s*\{#([\w-]+)\}\s*$', line)
                if m: c = {"id": m.group(2), "title": m.group(1), "lines": []}; chunks.append(c)
                elif c is not None: c["lines"].append(line)
            l["chunks"] = chunks
    return units

def attach_en(units, paths, md2html, inline, figs, cap_en, prof_en=None):
    en = parse(paths)
    assert [u["id"] for u in en] == [u["id"] for u in units], "unit ids differ"
    for u, ue in zip(units, en):
        u["title_en"] = ue["title"]; u["intro_en"] = ue["intro"]
        assert [l["id"] for l in ue["lessons"]] == [l["id"] for l in u["lessons"]], ("lesson ids differ", u["id"])
        for l, le in zip(u["lessons"], ue["lessons"]):
            l["title_en"] = le["title"]
            if le["exam"]: l["exam_en"] = le["exam"]
            assert [c["id"] for c in le["chunks"]] == [s["id"] for s in l["secs"]], ("section ids differ", l["id"])
            hs = []
            for s, c in zip(l["secs"], le["chunks"]):
                s["title_en"] = c["title"]
                pn = (prof_en or {}).get(c["id"])
                prof = f'<div class="callout prof"><b>Lecture note</b> <span class="src">{html.escape(pn[0])}</span><br>{inline(pn[1])}</div>' if pn else ''
                fg = ''.join(f'<figure class="slide"><button class="zoom" data-zoom="img/{f}.jpg" aria-label="Enlarge"><img src="img/{f}.jpg" alt="{html.escape(cap_en.get(f, cap))}" loading="lazy"></button><figcaption>{html.escape(cap_en.get(f, cap))}</figcaption></figure>' for f, cap in figs.get(c["id"], []))
                hs.append(f'<section class="sec" id="s-{c["id"]}"><h3>{inline(c["title"])}</h3>{md2html(c["lines"])}{prof}{fg}</section>')
            l["html_en"] = '\n'.join(hs)
    missing = [f for fl in figs.values() for f, _ in fl if f not in cap_en]
    assert not missing, ("captions missing", missing)
