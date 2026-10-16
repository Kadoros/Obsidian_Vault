# SQL·관계대수 풀이 문제 헬퍼: 정답 SQL을 교재 상태(SQLite)에서 실제로 돌려서 결과표를 정답에 붙인다
from qdsl import Q
import company as C

def _result(sql, db, expect):
    cols, rows = C.run(sql, db)
    if expect is not None:
        assert len(rows) == expect, (sql[:60], len(rows), expect, rows)
    return C.fmt(cols, rows), len(rows)

def SQLQ(id, concept, prompt, sql, db="company", check=None, expect=None, note=None, **kw):
    """sql = 보여줄 모범답안. check = SQLite에서 대신 돌릴 동치 SQL (ALL/ANY, 괄호 친 EXCEPT 등 SQLite가 못 읽을 때)"""
    tbl, n = _result(check or sql, db, expect)
    ans = sql.strip() + f"\n\n-- 교재 {'COMPANY' if db == 'company' else 'UNIVERSITY'} 상태에서 실행 결과 ({n}행)\n" + tbl
    if note: ans += "\n\n" + note
    Q(id, concept, "calc", prompt, ans, code=C.COMPANY_SCHEMA if db == "company" else C.UNIV_SCHEMA, **kw)

def RAQ(id, concept, prompt, ra, sql, expect=None, note=None, **kw):
    """ra = 모범답안 관계대수, sql = 같은 결과를 내는 SQL (검산용)"""
    tbl, n = _result(sql, "company", expect)
    ans = ra.strip() + f"\n\n-- COMPANY 상태에서의 결과 ({n}행)\n" + tbl
    if note: ans += "\n\n" + note
    Q(id, concept, "calc", prompt, ans, code=C.COMPANY_SCHEMA, **kw)

def rows(sql, db="company"):
    return C.run(sql, db)[1]
