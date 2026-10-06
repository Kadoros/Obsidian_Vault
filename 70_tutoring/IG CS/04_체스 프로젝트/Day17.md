---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: 체스 프로젝트
level: 표준
topic: "좌표 파싱 "e5" + 입력 검증"
---
1. **Parse Start Coordinate**: Change input to receive "e5". Calculate `startCol` using `ord(startCord[0]) - ord('a')` and `startRow` using `int(startCord[1]) - 1`.
    
      
    
2. **Update `moving` Function**: Apply the exact same parsing logic for the destination coordinate (`targetCord`) inside the `moving` function.
    
      
    
3. **Add Input Validation**: Use `if len(startCord) != 2:` right after the input to prevent program crashes.