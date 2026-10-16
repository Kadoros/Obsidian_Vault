CS = []
def C(id, concept, type, prompt, answer, **kw):
    q = {"id": id, "concept": concept, "type": type, "prompt": prompt}
    if type == "mc":
        q["choices"] = kw.pop("choices"); q["answer"] = answer
        assert 0 <= answer < len(q["choices"]), id
    elif type == "ox":
        q["answer"] = bool(answer)
    elif type == "blank":
        q["accept"] = kw.pop("accept"); q["answer"] = " / ".join(f"({chr(97+i)}) {a}" for i, a in enumerate(answer))
        assert len(q["accept"]) == len(answer), id
        assert prompt.count("(") >= len(answer), id
    else:
        raise ValueError(type)
    for k in ("explain", "code"):
        if k in kw: q[k] = kw.pop(k)
    assert not kw, (id, kw)
    CS.append(q)
