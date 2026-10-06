---
tags:
  - concept
parent_concept:
---
x86 어셈블리의 shift/rotate 계열 명령어 정리.

- **SHL / SHR**: 논리 시프트(Logical shift). 밀려나가는 비트는 CF(Carry Flag)에 저장됨. `SHL`은 ×2ⁿ, `SHR`은 ÷2ⁿ (unsigned)에 해당.
- **SAL / SAR**: 산술 시프트(Arithmetic shift). `SAL`은 `SHL`과 동일. `SAR`은 우측 시프트 시 **부호 비트(MSB)를 보존**하며 채워넣음 → signed 정수의 ÷2ⁿ.
- **ROL / ROR**: 캐리 플래그를 거치지 않고 비트를 순환(rotate)시킴. 밀려나간 비트가 반대쪽으로 그대로 들어감.
- **RCL / RCR**: 캐리 플래그를 9번째 비트(byte 연산 기준)로 포함해서 순환시킴. 즉 CF까지 포함한 더 큰 레지스터처럼 회전.
