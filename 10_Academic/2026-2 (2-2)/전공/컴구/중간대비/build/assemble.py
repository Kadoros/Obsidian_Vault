import json
d=json.load(open('data.json'))
s=open('template.html').read()
js=json.dumps(d,ensure_ascii=False).replace('</','<\\/')
open('ca-trainer.html','w').write(s.replace('/*DATA*/',js))
print(len(s), len(js))
