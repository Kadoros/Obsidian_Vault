from qdsl import Q, QS
Q("7-sse-2","static-scope-eval","ox","정적 영역은 프로그램이 수정·진화하면서 초기 구조가 무너져 전역 변수가 늘어나는 경향이 있다는 비판을 받는다.",True)
SLOTS={1:["1-crit-1","1-orth-1","1-rel-1","1-wr-1","1-simp-3"],2:["1-syn-1"],3:["1-hyb-1","1-phase-1"],
 4:["3-ss-1","3-ag-1"],5:["7-vc-1","7-sdb-1","7-tb-2"],6:["4-sep-1","4-ut-3","2-lt-2"],7:["6-adv-1","6-ls-2","5-rds-1"]}
PTS={1:3,2:3,3:3,4:3,5:3,6:3,7:3}
by={q["id"]:q for q in QS}
for s,ids in SLOTS.items():
    for i in ids: by[i]["slot"]=s; by[i]["pts"]=PTS[s]
