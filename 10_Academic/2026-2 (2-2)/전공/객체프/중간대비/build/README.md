# 객체프 중간 트레이너 빌드

라이브: https://claude.ai/artifact/Mz7gyUZZeB25YwCnfBaYci (capabilities: db, sample)
artifact 구성: `index.html`(= `page.html`) + `bank.json` + `learn.json` + `img/*.jpg` (페이지가 `fetch`로 읽음, 파일은 `../`에 있음)

## 소스
| 파일 | 내용 |
|---|---|
| `build_bank.py` | 문제은행 원본. `q(id, year, no, pts, type, topics, scope, prompt, answer, tip, code, src)` → 같은 폴더에 `bank.json` 생성 |
| `page.html` | 앱 본체. 2026-10-13에 **라이브 버전에서 받아온 것** ("오늘의 코스" 기능 포함). 옛 scratchpad의 `oop-midterm.html`은 그보다 이전 버전이라 버렸음 |
| `기출txt/` · `교안txt/` | 기출(2009–2025 중간, 2022 기말)과 교안 텍스트 추출본 |
| `cpp/` | 출력·추적 문제 정답을 실제로 컴파일해서 확인한 코드 |
| `learn/` | 학습 탭 원본. `lessons1–5.md` (`@unit`, `@lesson`, `## 섹션 {#개념id}`), `checks1–2.py` (이해 점검 199문제, `C(id, concept, mc/ox/blank, ...)`), `figs.py` (개념→슬라이드 그림), `build_learn.py` → `../../learn.json`. 개념→문제은행 topic 표 `T`가 '관련 기출' 버튼을 만듦 |
| `test/` | `smoke_claude.js`: 가짜 `window.claude`로 Claude 채점·db 기록·코스·채점 실패 폴백 검사 |

db 컬렉션: `attempts`, `checks` (학습 탭 점검 기록, attempts와 분리), `progress` (레슨 통과), `mocks`, `extra_questions`, `course/current` (Claude가 짜주는 코스: `{title, since, note, steps:[{qid|mock, stage, goal, pass}]}`)

## 빌드 → 검증 → 배포
```bash
python3 -B build_bank.py
python3 -B learn/build_learn.py           # learn.json
cd test && npm install && cd ..           # 처음 한 번 (jsdom)
node test/smoke_claude.js page.html ../bank.json ../learn.json   # 전부 통과 확인
```
배포는 Claude에게: `page.html`을 위 URL로 publish하고 `files`로 `bank.json`, `learn.json`, `img/*.jpg`를 같이 넘김.
- 슬라이드 그림: `pdftoppm -f N -l N -jpeg -jpegopt quality=72 -scale-to 1100 "교안.pdf"` → `../img/L03-p11.jpg` 식 이름.
- 점검 문제 id·개념 id도 바꾸지 말 것 (checks/progress가 연결됨).
- `capabilities`는 넘기지 않기 → db/sample 권한 유지.
- 문제 id를 바꾸거나 지우지 말 것 (attempts가 qid로 연결됨).
- `../객체프 중간 트레이너.html`: 오프라인 사본. `python3 -B offline.py`가 page.html에 bank·learn을 내장해서 만듦 (배포 후 같이 돌릴 것). 그림은 `../img/`.
- 기록 백업: 기록 탭 맨 위 '기록 내보내기/가져오기' (`../../../_shared/backup.js`, `patch_backup.py`로 4개 트레이너에 넣음). 배포 capabilities에 `downloads: true` 포함.
