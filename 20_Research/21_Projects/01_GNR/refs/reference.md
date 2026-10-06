---
tags:
  - project
parent_concept:
---
@article{ma2026physics,
  title={Physics-guided correction for operator learning under model misspecification},
  author={Ma, Lei and Boull{\'e}, Nicolas and Yang, Yu-Sen and Wu, Hao and Guo, Ling},
  journal={arXiv preprint arXiv:2606.03469},
  year={2026}
}

물리적 모델이 잘못 설정되거나 부정확한(Model misspecification) 상황에서, 물리 법칙을 기반으로 신경망 연산자의 예측 오차를 보정하는 기법을 제안합니다.

@article{yue2026deltaphi,
  title={DeltaPhi: Physical States Residual Learning for Neural Operators in Data-Limited PDE Solving},
  author={Yue, Xihang and Yang, Yi and Zhu, Linchao},
  journal={Advances in Neural Information Processing Systems},
  volume={38},
  pages={12701--12729},
  year={2026}
}


학습 데이터가 부족한(Data-limited) 환경에서 편미분방정식(PDE)을 효과적으로 풀기 위해, 물리적 상태의 잔차(Residual)를 학습하는 'DeltaPhi' 방법론을 제안합니다.


@article{um2020solver,
  title={Solver-in-the-loop: Learning from differentiable physics to interact with human 3D environments},
  author={Um, Kiwon and Brand, Robert and Fei, Yun (Ray) and Holl, Philipp and Thuerey, Nils},
  journal={Advances in Neural Information Processing Systems},
  volume={33},
  pages={6111--6122},
  year={2020}
}

미분 가능한 수치해석 솔버(FDM/FEM) 루프 안에 신경망을 직접 끼워 넣어, 수치해석의 잘림 오차나 놓친 디테일을 보정하는 Differentiable Physics의 대표작입니다.


@article{howard2023multifidelity,
  title={Multifidelity deep operator networks for data-driven and physics-informed problems},
  author={Howard, Amanda A and Perego, Mauro and Karniadakis, George Em and Stinis, Panos},
  journal={Journal of Computational Physics},
  volume={493},
  pages={112462},
  year={2023},
  publisher={Elsevier}
}



부정확한 물리 근사(Low-fidelity)를 뼈대로 삼고, 소량의 고신뢰도(High-fidelity) 실측 데이터를 Neural Operator로 매핑해 갭을 줄이는 다중 충실도 접근법입니다.

@article{yin2021augmenting,
  title={Augmenting physical models with deep networks for complex dynamics forecasting},
  author={Yin, Yuan and Le Guen, Vincent and Dona, J{\'e}r{\'e}mie and De B{\'e}zenac, Emmanuel and Ayed, Ibrahim and Thome, Nicolas and Gallinari, Patrick},
  journal={Journal of Statistical Mechanics: Theory and Experiment},
  volume={2021},
  number={12},
  pages={124012},
  year={2021},
  publisher={IOP Publishing and SISSA}
}

지배 방정식 중 아는 물리 법칙은 수학적 필터로 완전히 고정하고, 누락된 비선형 동역학(Missing physics) 항만을 딥러닝으로 추론해 기존 수식에 결합하는 LEADS 프레임워크입니다.

@article{kobayashi2025network,
  title={When network architecture meets physics: Deep operator learning for coupled multiphysics},
  author={Kobayashi, Kazuma and Park, Jaewan and Liu, Qibang and Koric, Seid and Abueidda, Diab and Bahauddin Alam, Syed},
  journal={arXiv e-prints},
  pages={arXiv--2507},
  year={2025}
}


거시적인 물리 상태를 입력받아, 기존 수치해석이 놓치는 다중 스케일(Multiscale)의 비선형 닫힘항(Closure term)을 DeepONet으로 학습해 예측하는 연구입니다.

@article{KANG2023105919,
title = {Learning subgrid-scale models with neural ordinary differential equations},
journal = {Computers & Fluids},
volume = {261},
pages = {105919},
year = {2023},
issn = {0045-7930},
doi = {https://doi.org/10.1016/j.compfluid.2023.105919},
url = {https://www.sciencedirect.com/science/article/pii/S0045793023001445},
author = {Shinhoo Kang and Emil M. Constantinescu},
keywords = {Neural ordinary differential equations, Machine learning, Acceleration, Coupling, Lorenz 96, Discontinuous Galerkin method},
abstract = {We propose a new approach to learning the subgrid-scale model when simulating partial differential equations (PDEs) solved by the method of lines and their representation in chaotic ordinary differential equations, based on neural ordinary differential equations (NODEs). Solving systems with fine temporal and spatial grid scales is an ongoing computational challenge, and closure models are generally difficult to tune. Machine learning approaches have increased the accuracy and efficiency of computational fluid dynamics solvers. In this approach neural networks are used to learn the coarse- to fine-grid map, which can be viewed as subgrid-scale parameterization. We propose a strategy that uses the NODE and partial knowledge to learn the source dynamics at a continuous level. Our method inherits the advantages of NODEs and can be used to parameterize subgrid scales, approximate coupling operators, and improve the efficiency of low-order solvers. Numerical results with the two-scale Lorenz 96 ODE, the convection–diffusion PDE, and the viscous Burgers’ PDE are used to illustrate this approach.}
}

난류나 충격파 등 수치해석 솔버 격자(Grid) 사이로 빠져나가는 미세 물리 현상(Subgrid-scale dynamics) 전체를 FNO(Fourier Neural Operator)로 추론하여 기존 솔버에 결합한 연구입니다.