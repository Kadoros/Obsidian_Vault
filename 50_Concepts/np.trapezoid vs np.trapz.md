---
tags:
  - concept
parent_concept:
---
NumPy의 사다리꼴 적분(trapezoidal rule) 함수 이름이 버전에 따라 다르다.

- `np.trapz`: 오래된 이름 (NumPy 2.0 이전, deprecated 됨)
- `np.trapezoid`: NumPy 2.0(2024)부터 추가된 새 이름, SciPy의 `scipy.integrate.trapezoid`와 이름 통일

둘은 완전히 동일한 사다리꼴 적분 함수이며, 환경의 NumPy 버전에 따라 한쪽만 존재할 수 있다. 호환성을 위한 패턴:

```python
if not hasattr(np, "trapezoid"):
    np.trapezoid = np.trapz
```
