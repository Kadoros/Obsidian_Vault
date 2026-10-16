# 객체프 중간 트레이너 빌드

라이브: https://claude.ai/artifact/Mz7gyUZZeB25YwCnfBaYci (capabilities: db, sample)
artifact 구성: `index.html`(= `page.html`) + `bank.json` (페이지가 `fetch("bank.json")`으로 읽음)

## 소스
| 파일 | 내용 |
|---|---|
| `build_bank.py` | 문제은행 원본. `q(id, year, no, pts, type, topics, scope, prompt, answer, tip, code, src)` → 같은 폴더에 `bank.json` 생성 |
| `page.html` | 앱 본체. 2026-10-13에 **라이브 버전에서 받아온 것** ("오늘의 코스" 기능 포함). 옛 scratchpad의 `oop-midterm.html`은 그보다 이전 버전이라 버렸음 |
| `기출txt/` · `교안txt/` | 기출(2009–2025 중간, 2022 기말)과 교안 텍스트 추출본 |
| `cpp/` | 출력·추적 문제 정답을 실제로 컴파일해서 확인한 코드 |
| `test/` | `smoke_claude.js`: 가짜 `window.claude`로 Claude 채점·db 기록·코스·채점 실패 폴백 검사 |

db 컬렉션: `attempts`, `mocks`, `extra_questions`, `course/current` (Claude가 짜주는 코스: `{title, since, note, steps:[{qid|mock, stage, goal, pass}]}`)

## 빌드 → 검증 → 배포
```bash
python3 -B build_bank.py
cd test && npm install && cd ..           # 처음 한 번 (jsdom)
node test/smoke_claude.js page.html bank.json   # 전부 통과 확인
```
배포는 Claude에게: `page.html`을 위 URL로 publish하고 `files: {"bank.json": "bank.json"}`을 같이 넘김.
- `capabilities`는 넘기지 않기 → db/sample 권한 유지.
- 문제 id를 바꾸거나 지우지 말 것 (attempts가 qid로 연결됨).
- `../객체프 중간 트레이너.html`은 bank를 내장한 오프라인용 옛 사본이고, 코스 기능이 없음.
