---
tags:
  - concept
parent_concept:
  - "[[50_Concepts/x86 Stack Frame|x86 Stack Frame]]"
---
`PUSHAD` / `POPAD`는 x86의 8개 범용 레지스터(EAX, ECX, EDX, EBX, ESP, EBP, ESI, EDI)를 한 번에 스택에 저장/복원하는 명령어다.

- `PUSHAD`: 8개 레지스터 × 4바이트 = **32바이트**를 스택에 push
- `POPAD`: 동일하게 32바이트를 pop하여 레지스터 복원

함수 내부에서 여러 레지스터를 마음대로 사용하면서도 호출자의 레지스터 상태를 보존해야 할 때, 일일이 push/pop하는 대신 한 쌍으로 처리할 수 있다.
