# DB 중간 트레이너 빌드

라이브: https://claude.ai/artifact/HJGqU6QWPPqVTAfu2i4ER8 (capabilities: db, sample, user)
출력물: `../DB 중간 트레이너.html`, `../bank.json`, 그림은 `../img/` (artifact엔 `img/*.jpg`로 올라가 있음)
구조는 프밍언 트레이너(`프밍언/중간대비/build`)와 같음. 템플릿만 과목 설정(`config.py`의 META)을 읽게 바꿈.

## 소스
| 파일 | 내용 |
|---|---|
| `lessons1–6.md` | 레슨 본문. `@unit U1 \| 제목 \| 교안`, `@intro`, `@lesson L1-1 \| 제목 \| 교안 쪽`, `## 섹션 {#concept-id}` (섹션 id = 개념 id) |
| `qdsl.py` | 문제 DSL `Q(id, concept, type, prompt, answer, choices/accept/keys/code/explain)` |
| `sq.py` | `SQLQ` / `RAQ`: 정답 SQL(관계대수는 같은 결과의 SQL)을 SQLite에서 돌려 결과표를 정답에 붙이고 `expect` 행 수를 assert |
| `company.py` | 교재 COMPANY(교안 3-1 p.12)·UNIVERSITY 상태 + 문제에 붙이는 스키마 요약 |
| `q1–q6.py` | 단원별 문제, `q7.py` = 모의고사 슬롯 배정 |
| `config.py` | 개념 가중치, 예상 시험지(BLUEPRINT·SLOTS·DIST), 대시보드 메모. **기출을 받으면 여기를 고칠 것** |
| `prof.py` / `figs.py` | 개념 → 수업 메모 (03주-2, 05주-1 전사) / 개념 → 슬라이드 그림 |
| `template.html` | 앱 본체. `/*DATA*/` 자리에 data.json이 들어감 |
| `교안txt/` | 교안 텍스트 추출본 |
| `test/` | jsdom 스모크 테스트 |

## 빌드 → 검증 → 배포
```bash
python3 -B build.py && python3 -B assemble.py      # data.json, bank.json, db-trainer.html (SQL 정답 실행 검산 포함)
cd test && npm install && cd ..                      # 처음 한 번 (jsdom)
for t in smoke smoke2 smoke3 smoke_claude; do node test/$t.js db-trainer.html; done
cp db-trainer.html "../DB 중간 트레이너.html"; cp bank.json ../bank.json
```
배포는 Claude에게: `../DB 중간 트레이너.html`을 위 URL로 publish. `files`·`capabilities`는 넘기지 않기 (기존 이미지와 권한 유지). 문제 id는 바꾸거나 지우지 말 것 (db attempts가 qid로 연결). 새 문제는 새 id로, 또는 db `extra_questions`에 `concept`를 지정해 넣으면 재배포 없이 병합됨.

## 남은 것
- 10/13 Functional Dependencies and Normalization 교안이 없어서 빠져 있음 (범위 확인 필요)
- 기출 받으면 `config.py` BLUEPRINT/SLOTS/DIST 교체, 기출 유형 변형 문제 추가
