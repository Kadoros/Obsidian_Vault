# 개념 가중치(점검 때 개념당 문제 수), 모의고사 구성, 홈·대시보드 안내문
W3 = """perf-ratio cpu-time cpi weighted-cpi amdahl mips-metric lw-sw endian twos sign-ext r-format i-format encode-example
if-else while-loop leaf nonleaf fact-trace branch-addr overflow mult-v1 mult-v2 div-v1 ieee-examples ieee-format
mux-basic composing dp-rtype dp-lw dp-sw dp-beq mux-trap branch-calc control-table aluop offset-const""".split()
W1 = """course-info classes-ideas below-program spec-idle mips-classes reg-vs-mem hex fallacies translate addr-modes lui-ori
mult-instr div-v2 fp-instr kmap control-logic clocking branch-instr int-add mult-basic div-example stack-size""".split()
WEIGHTS = {c: 3 for c in W3}
WEIGHTS.update({c: 1 for c in W1})   # 나머지는 2

MOCK = {
  "label": "예상 형식 (10/14 유형 안내 전 추정)", "mins": 120,
  "desc": "서술 3점(영어) → 성능 계산 → 엔디안·2의 보수 → C→MIPS·인코딩 → if/while·프로시저 → 곱셈·나눗셈 과정 → IEEE 754 → 제어 신호·분기 오프셋·데이터패스 서술. 매번 안 푼 변형 위주로 뽑아.",
  "slots": [{"slot":1,"pts":3},{"slot":2,"pts":3},{"slot":3,"pts":6},{"slot":4,"pts":6},{"slot":5,"pts":5},{"slot":6,"pts":5},
            {"slot":7,"pts":6},{"slot":8,"pts":6},{"slot":9,"pts":8},{"slot":10,"pts":8},{"slot":11,"pts":8},{"slot":12,"pts":7},
            {"slot":13,"pts":6},{"slot":14,"pts":8},{"slot":15,"pts":6},{"slot":16,"pts":9}],
}

EXAM_NOTES = [
  "**10/20 (화) 17:00–19:00**, 아마 이 수업 강의실. 못 오면 교수님께 이메일 (06주-2).",
  "범위: 첫 수업 ~ 10/12 수업 (Processor 단순 버전, 교안 week6 p.32 '제어 신호 표'까지). 파이프라인은 기말.",
  "**영어로 출제, 영어로 답안.** closed book.",
  "중간엔 수업에서 정한 명령어만. 다른 명령어를 쓰면 0점 (06주-1).",
  "lw/sw offset은 반드시 상수. 레지스터를 offset에 쓰면 0점, OX면 False (3·4·6주 반복 강조).",
  "수업 예제가 시험과 아주 비슷하게 나온다 (02주-1). 형식 예고: 명령어·설명을 주고 빈칸/MIPS 표현 채우기 (05주-1).",
  "ALU control 표 같은 표는 시험에 주어짐. 읽고 회로에 적용할 줄 알면 됨 (06주-2).",
  "10/14(수) 수업에서 시험 유형 안내 예정 → 녹음 들어오면 모의고사 구성 갱신.",
]
HOME_NOTES = [
  "교안 week1–6 전부 + 수업 녹음 전사 10개 기반. 교수님이 든 예시·강조는 각 섹션의 **수업 메모** 박스에 넣었어.",
  "6주(데이터패스)는 **수업 따라가기** 탭에서 녹음 타임스탬프별로 슬라이드의 해당 부분만 밝혀서 볼 수 있어. 판서·말실수도 표시.",
  "계산 문제 정답(곱셈·나눗셈 단계표, IEEE 754, 인코딩, ALU control)은 전부 코드로 검산한 값.",
  "교안 오타 3개: week3 p.21 부호 확장 예, week6 p.30 K-map 식(NOT 누락), week3 p.47 fact의 `return f`.",
  "03주-2(9/21)는 결석으로 녹음 없음, 05주-2는 대체공휴일.",
]
