---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: 체스 프로젝트
level: 심화
topic: "폰 2칸 전진, 룩 추가, 승리 판정"
---
폰 첫 2칸 전진: 폰이 시작 행에 있고 1칸 앞과 2칸 앞이 모두 빈칸(.)일 때만 2칸 앞까지 X 표시하기. (1칸 앞이 막히면 2칸 앞도 불가)


새 기물 룩(R/r) 추가: 보드에 R, r을 배치하고 상·하·좌·우로 직진하다가 기물을 만나면 멈추는(break) show_R_path 함수 구현 및 while문에 연결하기.

게임 종료(승리 판정): moving 함수에서 이동한 목표 위치에 있던 기물이 K나 k라면 게임 종료! [승리팀] 승리!를 출력하고 프로그램(break) 종료하기.