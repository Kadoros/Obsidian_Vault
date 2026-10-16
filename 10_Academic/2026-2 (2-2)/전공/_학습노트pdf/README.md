# 과목별 학습 노트 PDF 만들기

트레이너 학습 탭의 레슨 본문(그림·수업 메모 포함)을 A4 PDF로 뽑는다. 결과: 각 과목 `중간대비/<과목> 학습 노트.pdf`, 영어A 과목(컴구·DB·객체프)은 `<과목> 학습 노트 (English).pdf`도

```bash
W=/tmp/notepdf; mkdir -p $W; cp note.css $W/
(cd ../컴구/중간대비/build && python3 -B build.py)   # 컴구 data.json은 gitignore라 먼저 빌드
python3 mk.py $W                                  # 과목별 HTML
NODE_PATH=$(npm root -g) node pdf.js $W/jobs.json # Chromium(playwright)으로 PDF
```
프밍언·DB는 `build/data.json`, 객체프는 `learn.json`을 그대로 읽으니 레슨을 고쳤으면 그 과목 빌드부터 다시 돌릴 것.

## 영어판
- 원본: 각 빌드 폴더의 `lessonsN.en.md` (한국어판과 `@unit`·`@lesson`·`{#개념id}`가 똑같아야 함), `figs_en.py`(`CAP_EN`), `prof_en.py`(`PROF_EN`, 컴구·DB).
- 빌드가 `../_shared/en_lessons.py`의 `attach_en`으로 `title_en`·`intro_en`·`html_en`을 붙이고, id가 어긋나면 assert.
- 트레이너 학습 탭 왼쪽 위 **한국어 / English** 버튼이 이 필드를 씀 (`_shared/patch_lang.py`로 템플릿에 넣었음, 선택은 localStorage `ca-lang`/`db-lang`/`oop-lang`).
- 한국어 노트를 고치면 같은 곳의 `.en.md`도 같이 고칠 것.
