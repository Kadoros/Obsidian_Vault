---
tags:
  - concept
parent_concept:
---
NaN(Not a Number)이 코드에 등장한다고 항상 "에러"인 것은 아니다. 흔한 두 가지 발생 패턴:

1. **딕셔너리에 키가 없을 때 기본값으로 사용**
   ```python
   value = gp_res.get("hx_floor", float("nan"))
   ```
   → 해당 값이 아직 계산/저장되지 않았음을 의미

2. **계산이 정의되지 않을 때 명시적으로 반환**
   ```python
   ratio = a / b if b != 0 else float("nan")
   ```
   → 분모가 0이거나 조건이 안 맞아 "정의되지 않은 값"임을 의미

즉 NaN은 "이 값은 아직 정의/계산되지 않았다"는 신호로 쓰이는 경우가 많으며, 발생 위치를 보고 어느 케이스인지 구분해야 한다.
