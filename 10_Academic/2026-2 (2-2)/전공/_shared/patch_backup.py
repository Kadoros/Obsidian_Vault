# python3 patch_backup.py <template> <prefix> <과목 이름>  — 기록 백업 블록을 boot() 호출 앞에 넣고, 맨 앞에 meta charset
import sys, os
p, pfx, name = sys.argv[1:4]
s = open(p).read(); assert "bkExport" not in s, "already"
js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backup.js")).read()
anchor = "\nboot();\n"; assert s.count(anchor) == 1, p
s = s.replace(anchor, f'\nconst BK_PFX = "{pfx}", BK_NAME = "{name}";\n' + js + anchor)
if "charset" not in s[:300]: s = '<meta charset="utf-8">\n' + s
open(p, "w").write(s); print("ok", p)
