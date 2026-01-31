---
tags:
  - Paper
  - SLAM
parent_concept: "[[../../../50_Concepts/SLAM|SLAM]]"
status: 1st Reading
date: 2026-01-27
paper_link: https://arxiv.org/abs/2412.12392
pdf: "[[PDF/MASt3R-SLAM_pdf.pdf]]"
code_link:
---

# 요약
- 

# Sections
# Abstract
- This paper present a real-time monocular [[../../../50_Concepts/dense SLAM|dense SLAM]] system designed bottom-up from [[../../../50_Concepts/MASt3R]], a two-view 3D reconstruction and matching prior.
- MASt3R의 강력한 능력 지능
- 와일드한 현장에서 강함
- 카메라 정보 필요 없음 (plug-and-play)
	- 만약 있으면 정확도 확 상승
- Efficient Pointmap Matching, 
	- MASt3R는 무거움 이걸 해결함
- Camera Tracking and Local Fusion
- Graph Construction and Loop Closure
	- 카메라 경로 그래프 형태로 , Loop Closure로 오차 잡음
- Second-order Global Optimisation
- 실시간으로 구동  15fps

# System Flaw


