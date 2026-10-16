QS=[]
def Q(id, concept, type, prompt, answer, **kw):
    q={"id":id,"concept":concept,"type":type,"prompt":prompt}
    if type=="mc": q["choices"]=kw.pop("choices"); q["answer"]=answer
    elif type=="ox": q["answer"]=bool(answer)
    elif type=="blank":
        q["answer"]=" / ".join(f"({chr(97+i)}) {a}" for i,a in enumerate(answer)); q["accept"]=kw.pop("accept")
    else: q["answer"]=answer
    for k in ("code","explain","keys","slot","pts"):
        if k in kw: q[k]=kw.pop(k)
    assert not kw, (id, kw)
    QS.append(q)
