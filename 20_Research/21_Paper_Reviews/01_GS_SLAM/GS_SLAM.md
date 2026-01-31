---
tags:
  - Paper
  - SLAM
parent_concept: "[[../../../50_Concepts/SLAM|SLAM]]"
status: 2st Reading
date: 2026-01-27
paper_link: https://arxiv.org/abs/2311.11700
pdf: "[[PDF/GS_SLAM_PDF.pdf]]"
code_link:
---

# 요약
- 처음으로  [[../../../50_Concepts/3D Gaussian representation|3D Gaussian representation]] 을 이용한  [[../../../50_Concepts/SLAM|SLAM]] 
- 다른 것들은 3프래임 나올떄 이녀석은 300프래임 넘꼐 나옴 
- 기본적으로 RGB-D 입력을 받음 
	- 만약 이걸 적외선으로 받는 다면 불나면 무용지물
- 메모리가 4배정도 많이씀

# 내 생각
- 만약 적외선으로 d값을 안받는 다면 화제 환경에서도 사용 가능 할 듯 
- 메모리가 많이 쓰이니까 서버에서 돌리는 면 될지도 
- 여기에는 loop closure 나 전역 최적화가 논의 되지 않음
	- 걍 3dgs들을 어떤 부분을 한 구역으로 나누고 그 구역의 중심(카메라의 이동위치)를  그래프의 노드로 하고 강제로 움직이고 그리고 최적화 하면 될지도 
# Sections


# System Flaw


