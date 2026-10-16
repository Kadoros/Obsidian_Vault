# 컴구 중간 트레이너 빌드

라이브: https://claude.ai/artifact/Y2pfBBuTZ7ghMCa3TKad6W (capabilities: db, sample, user)
출력물: `../컴구 중간 트레이너.html`, `../bank.json`, `../컴구 중간 정리.md`, 그림은 `../img/` (artifact엔 `img/*.jpg`로 올라감)
엔진은 프밍언 트레이너 템플릿 기반 (`프밍언/중간대비/build/`). 저장 키는 `ca-` 접두사라 프밍언 기록과 안 섞임.

## 소스
| 파일 | 내용 |
|---|---|
| `lessons1–4.md` | 레슨 본문. `@lesson L1-1 \| 제목 \| 교안 쪽 \| 시험 포인트(대시보드 노란 칸)`, `## 섹션 {#concept-id}` |
| `q1–q5.py` + `qdsl.py` | 문제. 유형 mc/ox/blank/short/calc + **sig**(제어 신호 0/1/X 표, 자동 채점) |
| `meta.py` | 개념 가중치, 모의고사 slot·배점(현재 추정 형식), 시험 공지·홈 메모 |
| `prof.py` / `figs.py` | 개념 → 수업 메모 / 개념 → 슬라이드 그림 |
| `walk.py` | **6주 수업 따라가기**: 녹음 타임스탬프별 장면(슬라이드, 밝힐 영역, 신호 경로, 태그, 칠판, 말실수·추정 플래그) + 데이터패스 놀이터 |
| `regions_dp.json` / `paths_dp.json` | week6 p.3 데이터패스의 컴포넌트 박스·와이어 경로 좌표(%) |
| `sim.py` | 검산기: 곱셈·나눗셈 하드웨어 단계표, IEEE 754, MIPS 인코딩, 제어 신호 표, ALU control(K-map 보정식) |
| `template.html` | 앱 본체 |
| `test/` | jsdom 스모크: `smoke_claude.js`(Claude 채점·db), `smoke3.js`(자동 통과), `smoke_walk.js`(수업 따라가기·sig·모의고사) |

## 빌드 → 검증 → 배포
```bash
python3 -B sim.py                                  # 계산 정답 확인
python3 -B build.py && python3 -B assemble.py      # 개념·문항·장면 무결성 assert
cd test && npm install && cd ..
for t in smoke_claude smoke3 smoke_walk; do node test/$t.js ca-trainer.html; done
cp ca-trainer.html "../컴구 중간 트레이너.html"; cp bank.json ..; cp 정리.md "../컴구 중간 정리.md"
```
배포는 Claude에게: `../컴구 중간 트레이너.html`을 위 URL로 publish. `capabilities`·`files`는 넘기지 않기 (권한·이미지 유지). 새 슬라이드 그림을 추가했을 때만 그 파일을 `files`로.
- 문제 id 바꾸거나 지우지 말 것 (attempts가 qid로 연결).
- 재배포 없이 변형문제: db `extra_questions`에 `concept` 지정.

## 장면 추가 방법 (walk.py)
`dict(t="12:04", t2="12:42", slide=3, h="제목", concept="개념id", focus=R("mux_regdst"), paths=P("c_regdst"), marks=[M(x,y,"텍스트","sig",ax,ay)], say=…, quote=…, board=…, flags=["exam"|"slip"|"board"|"guess"|"mine"], note=…)`.
타임스탬프는 `녹음/*.segments.json` 기준. 새 슬라이드 쪽이 필요하면 `used_pages()`가 잡아서 `img/w6-pNN.jpg`로 렌더(빌드 전 렌더 스크립트 필요: pdftoppm -jpeg -r 130).

## 남은 일
- 10/14(수) 수업: 교수님이 시험 유형을 안내할 예정 → 녹음 전사 후 `meta.MOCK` slot 구성과 문제 형식을 맞추기.
