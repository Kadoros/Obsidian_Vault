# 프밍언 중간 트레이너 빌드

라이브: https://claude.ai/artifact/CVvjvQctxQtRS6oQDMDHDR (capabilities: db, sample, user)
출력물: `../프밍언 중간 트레이너.html`, `../bank.json`, 그림은 `../img/` (artifact엔 `img/*.jpg`로 올라가 있음)

## 소스
| 파일 | 내용 |
|---|---|
| `lessons1–5.md` | 레슨 본문. `@unit U1 \| 제목 \| 교안`, `@intro`, `@lesson L1-1 \| 제목 \| 교안 쪽`, `## 섹션 {#concept-id}` (섹션 id = 개념 id) |
| `qdsl.py` | 문제 DSL `Q(id, concept, type, prompt, answer, choices/accept/keys/code/explain/slot/pts)` |
| `q1–q9.py` | 문제 (q7 = 24 족보 서술 slot 배정, q8 = 개념 가중치 `W3`/`W1` + 보강, q9 = 전사 기반) |
| `prof.py` / `figs.py` | 개념 → 수업 메모 / 개념 → 슬라이드 그림 |
| `gram.py` `lr.py` `rd.py` | 계산 문제 정답 검산기 (FIRST·집합쌍·모호성 / LR 추적 / 재귀하강 추적) |
| `template.html` | 앱 본체(JS·CSS). `/*DATA*/` 자리에 data.json이 들어감 |
| `교안txt/` | 교안·24 족보 텍스트 추출본 (문제 만들 때 참고) |
| `test/` | jsdom 스모크 테스트. `smoke_claude.js`는 가짜 `window.claude`로 Claude 채점·db 기록 경로 검사 |

## 빌드 → 검증 → 배포
```bash
python3 -B build.py && python3 -B assemble.py      # data.json, bank.json, pl-trainer.html 생성 (assert로 id·concept·정답 검사)
cd test && npm install && cd ..                      # 처음 한 번 (jsdom)
for t in smoke smoke2 smoke3 smoke_claude; do node test/$t.js pl-trainer.html; done   # ERRORS [] / 전부 통과 확인
cp pl-trainer.html "../프밍언 중간 트레이너.html"; cp bank.json ../bank.json
```
배포는 Claude에게: `../프밍언 중간 트레이너.html`을 위 URL로 publish.
- `files`·`capabilities`는 **넘기지 않기** → 기존 이미지와 db/sample/user 권한이 그대로 유지됨. `capabilities: {}`를 넘기면 Claude 채점·클라우드 기록이 꺼짐.
- 문제 id를 바꾸거나 지우지 말 것. db의 attempts가 qid로 연결돼 있어서 기록이 고아가 됨. 새 문제는 새 id로.
- 재배포 없이 문제만 추가할 때는 db `extra_questions`에 `concept`를 지정해서 넣으면 페이지가 자동으로 병합함.

## 고친 것
- 2026-10-13: db가 연결된 상태에서 점검 퀴즈를 맞히면 결과 화면 없이 다음 문제로 넘어가던 버그. 저장 직후 db 스냅샷이 화면을 다시 그리면서 `autoCarry`가 방금 기록을 "전에 맞힌 문제"로 처리했음. 이제 퀴즈 시작(`quiz.start`) 이전 기록만 자동 통과로 침. `start`가 없는 예전 진행 중 퀴즈는 페이지를 연 시각(`BOOT`) 이전 기록 기준 (v9).
