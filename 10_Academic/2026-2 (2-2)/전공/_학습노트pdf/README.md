# 과목별 학습 노트 PDF 만들기

트레이너 학습 탭의 레슨 본문(그림·수업 메모 포함)을 A4 PDF로 뽑는다. 결과: 각 과목 `중간대비/<과목> 학습 노트.pdf`

```bash
W=/tmp/notepdf; mkdir -p $W; cp note.css $W/
cp -r ../컴구/중간대비/build $W/cg && (cd $W/cg && python3 -B build.py)   # 컴구 data.json은 git에 없어서 사본에서 빌드
python3 mk.py $W                                  # 과목별 HTML
NODE_PATH=$(npm root -g) node pdf.js $W/jobs.json # Chromium(playwright)으로 PDF
```
프밍언·DB는 `build/data.json`, 객체프는 `learn.json`을 그대로 읽으니 레슨을 고쳤으면 그 과목 빌드부터 다시 돌릴 것.
