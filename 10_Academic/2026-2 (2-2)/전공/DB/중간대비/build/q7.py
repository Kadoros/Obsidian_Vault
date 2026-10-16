# 예상 시험지 슬롯 배정 (config.SLOTS) — 문제 정의 파일을 다 읽은 뒤에 import할 것
from qdsl import QS
from config import SLOTS, BLUEPRINT
PTS = {s: p for _, s, p in BLUEPRINT}
by = {q["id"]: q for q in QS}
for s, ids in SLOTS.items():
    for i in ids:
        assert i in by, i
        assert by[i]["type"] in ("short", "calc"), (i, by[i]["type"])
        by[i]["slot"] = s; by[i]["pts"] = PTS[s]
