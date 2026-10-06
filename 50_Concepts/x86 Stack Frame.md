---
tags:
  - concept
parent_concept:
---
x86 함수 호출 시 스택 프레임 구성 방식 (cdecl 계열).

**Prologue**
```asm
push ebp        ; 이전 프레임의 base pointer 저장
mov ebp, esp    ; 현재 esp를 새 base pointer로
```

**인자 접근**: 호출자가 push한 인자는 `[ebp+8]`이 첫 번째 인자 (`[ebp+4]`는 리턴 주소, `[ebp]`는 saved ebp).

**Epilogue**
```asm
pop ebp
ret N           ; N = 호출자가 push한 인자 바이트 수, 리턴하면서 스택 정리
```

재귀 호출 시 매 호출마다 이 프레임이 스택에 쌓이며, 함수가 리턴할 때마다 한 프레임씩 해제된다.
