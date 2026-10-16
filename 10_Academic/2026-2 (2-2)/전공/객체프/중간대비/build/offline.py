# page.html + bank.json + learn.json → ../객체프 중간 트레이너.html (브라우저로 바로 여는 오프라인 사본, 그림은 ../img/)
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
emb = {n: json.load(open("../" + n)) for n in ("bank.json", "learn.json")}
js = json.dumps(emb, ensure_ascii=False).replace("</", "<\\/")
s = open("page.html").read()
s = s.replace('<meta charset="utf-8">\n', '<meta charset="utf-8">\n<script>window.__EMBED = ' + js + ';</script>\n', 1)
assert "__EMBED = " in s
open("../객체프 중간 트레이너.html", "w").write(s); print("ok", len(s))
