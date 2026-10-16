# 과목 설정: 개념 가중치, 예상 시험지(모의고사 슬롯), 화면에 나오는 메모
# 기출(족보)을 받으면 BLUEPRINT·DIST·SLOTS를 그 형식에 맞게 바꿀 것

# 레슨 점검 퀴즈에서 개념마다 몇 문제를 낼지 (기본 2)
W3 = """data-indep three-schema attr-types cardinality participation minmax weak-entity superkey-key ref-integrity
op-insert op-update map-11 map-1n map-mn ref-actions sfw multiset-distinct nested-in exists division-sql
inner-outer group-by having view-update ra-select ra-project ra-join ra-division ra-practice-join ra-practice-diff""".split()
W1 = """why-dbms when-not design-process initial-design rel-model sql-intro drop schema-mapping view-auth ra-intro
join-size ra-agg-props""".split()
WEIGHTS = {c: 3 for c in W3}
WEIGHTS.update({c: 1 for c in W1})

# 예상 시험지: (레슨, 슬롯, 배점) — 합 100
BLUEPRINT = [
 ["L1-2",1,3],["L1-3",2,3],["L3-2",3,3],["L5-6",4,3],["L6-1",5,3],["L5-5",6,3],
 ["L2-2",7,5],["L3-3",8,5],["L4-2",9,5],
 ["L2-4",10,10],["L3-5",11,10],["L4-4",12,10],["L5-2",13,10],["L5-4",14,10],["L6-6",15,10],
 ["L6-4",16,7],
]
assert sum(p for _,_,p in BLUEPRINT) == 100

SLOTS = {
 1: ["1-char-5","1-char-2","1-abs-3","1-share-3"],
 2: ["1-di-4","1-3s-4","1-dm-4"],
 3: ["3-key-5","3-ri-4","3-ei-2"],
 4: ["5-vu-2","5-vu-3","5-vi-3","5-vd-5"],
 5: ["6-in-2","6-qt-3","6-jn-5"],
 6: ["5-tr-3","5-tr-5","5-as-2"],
 7: ["2-mm-5","2-mm-7"],
 8: ["3-ins-5","3-del-4","3-upd-5"],
 9: ["4-ra-4","4-ra-5","4-ra-6"],
 10: ["2-prac-4","2-prac-6","2-ref-5"],
 11: ["3-ms-4","3-ms-5","3-mw-4","3-mmn-4"],
 12: ["4-sfw-5","4-sfw-6","4-qa-3","4-qa-5","4-ob-1"],
 13: ["5-div-4","5-div-5","5-div-6","5-ex-4","5-ex-3"],
 14: ["5-hv-3","5-hv-2","5-gb-5","5-hv-5"],
 15: ["6-pu-1","6-pd-1","6-pd-2","6-pj-1","6-div-3"],
 16: ["6-div-2","4-so-2","6-set-6"],
}

DIST = [
 [30, "SQL 작성: 기본 조인, 중첩·EXISTS·나눗셈, GROUP BY·HAVING (12–14번)"],
 [20, "ER 설계와 ER→관계 매핑 (10, 11번)"],
 [17, "관계 대수 작성과 나눗셈·집합 연산 계산 (15, 16번)"],
 [15, "(min,max), 제약 위반 판정, 참조 트리거 동작 (7–9번)"],
 [18, "개념 서술 3점 × 6: DB 특징, 3단계 스키마, 키·무결성, 뷰, 관계 대수, Assertion·Trigger (1–6번)"],
]

META = {
 "mockMin": 75,
 "mockLabel": "예상 시험지 (기출 받기 전 임시)",
 "mockNote": "개념 서술 3점 6개 → (min,max)·제약 위반·참조 동작 5점 → ER 설계·매핑·SQL 3개·관계 대수 10점 → 계산 7점. 매번 안 푼 변형 위주로 뽑아.",
 "blueprint": BLUEPRINT,
 "dist": DIST,
 "notes": [
  "중간고사 <b>10/23(금)</b> (교안 일정표 기준). 범위는 교안 1~6 (Course Intro → Relational Algebra) + 실습 자료. 시험은 closed-book, 중간 40%.",
  "⚠️ 10/13(화) <b>Functional Dependencies and Normalization</b> 수업은 일정표상 중간 전 마지막 수업인데 교안이 폴더에 없어서 여기 안 들어 있어. 범위에 들어가는지 확인해 줘.",
  "기출이 아직 없어서 모의고사 구성과 '예상 배점'은 교안 비중으로 잡은 임시 구성이야. 기출을 받으면 그 형식에 맞춰 바꿀게.",
  "SQL·관계 대수 풀이 문제의 정답 결과표는 교재 COMPANY 상태(교안 3-1 p.12)를 SQLite에 올려서 실제로 돌린 결과야. 다른 풀이도 결과가 같으면 맞는 답.",
  "수업 녹음은 03주-2(실습 환경, 조교)와 05주-1(Advanced SQL)뿐이라 <b style=\"color:var(--accent)\">수업 메모</b>는 U4·U5에만 있어.",
  "교안 오타로 보이는 곳: 2 p.42 SUPERVISION 1쪽/N쪽 설명이 뒤바뀜, db-exercises Q2는 = 대신 IN이 맞음, 연습 2 풀이의 E.Dno = P.Dnum은 W.Pno = P.Pnumber가 맞음. 해당 문제 해설에 적어 놨어.",
 ],
}
