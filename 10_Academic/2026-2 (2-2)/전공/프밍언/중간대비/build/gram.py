import itertools
def parse(g):  # "S -> aAb | bBA ; A -> ab"
    G={}
    for r in g.split(';'):
        l,rhs=r.split('->'); G[l.strip()]=[a.strip() for a in rhs.split('|')]
    return G
def first(G):
    F={n:set() for n in G}
    ch=True
    while ch:
        ch=False
        for n,alts in G.items():
            for a in alts:
                f=fs(G,F,a)
                if not f<=F[n]: F[n]|=f; ch=True
    return F
def fs(G,F,s):
    out=set()
    for c in s:
        if c=='ε': continue
        if c in G:
            out|=F[c]-{'ε'}
            if 'ε' not in F[c]: return out
        else: out.add(c); return out
    out.add('ε'); return out
def pdt(g):
    G=parse(g);F=first(G)
    for n,alts in G.items():
        if len(alts)<2: continue
        sets=[(a,fs(G,F,a)) for a in alts]
        bad=[(x[0],y[0],x[1]&y[1]) for x,y in itertools.combinations(sets,2) if x[1]&y[1]]
        print(n,':',', '.join(f'FIRST({a})={sorted(s)}' for a,s in sets),'->','FAIL '+str(bad) if bad else 'PASS')
# handle finder: search trees by rightmost derivations (BFS) whose frontier == target
def trees(g,target,start='S',maxlen=None):
    G=parse(g); maxlen=maxlen or len(target)+2
    res=[]
    # node: (sym, children or None)
    def frontier(t):
        s,ch=t
        if ch is None: return [t]
        out=[]
        for c in ch: out+=frontier(c)
        return out
    def string(t): return ''.join(n[0] for n in frontier(t)) 
    import copy
    # explore by expanding any nonterminal leaf (all positions) - dedupe by tree repr
    def rep(t):
        s,ch=t
        return s if ch is None else s+'('+','.join(rep(c) for c in ch)+')'
    seen=set(); frontierq=[(start,None)]
    q=[(start,None)]
    found={}
    while q:
        t=q.pop()
        r=rep(t)
        if r in seen: continue
        seen.add(r)
        st=string(t)
        if st==target: found[r]=t
        if len(st.replace('ε',''))>maxlen: continue
        # expand each unexpanded NT leaf
        leaves=frontier(t)
        for i,(sym,ch) in enumerate(leaves):
            if sym in G:
                for alt in G[sym]:
                    q.append(expand(t,i,alt))
    return list(found.values()),rep
def expand(t,idx,alt):
    cnt=[0]
    def go(n):
        s,ch=n
        if ch is None:
            if cnt[0]==idx:
                cnt[0]+=1
                return (s,[(c,None) for c in alt])
            cnt[0]+=1; return n
        return (s,[go(c) for c in ch])
    return go(t)
def analyze(g,target):
    ts,rep=trees(g,target)
    print('==',target,'trees:',len(ts))
    for t in ts:
        print(' tree:',rep(t))
        phrases=[];simple=[]
        pos=[0]
        def walk(n):
            s,ch=n
            if ch is None:
                p=pos[0]; pos[0]+=1; return (p,p+1,s)
            parts=[walk(c) for c in ch]
            a,b=parts[0][0],parts[-1][1]
            y=''.join(p[2] for p in parts)
            phrases.append((a,y,s))
            if all(c[1] is None for c in ch): simple.append((a,y,s))
            return (a,b,y)
        walk(t)
        print('  phrases:',[f'{y}({s}@{a})' for a,y,s in sorted(phrases)])
        print('  simple :',[f'{y}({s}@{a})' for a,y,s in sorted(simple)])
        print('  handle :',min(simple)[1], 'at', min(simple)[0])
def rsf(g,start='S',maxlen=7):
    G=parse(g); out=set(); q=[start]; seen=set()
    while q:
        s=q.pop()
        if s in seen: continue
        seen.add(s); out.add(s)
        idx=max((i for i,c in enumerate(s) if c in G),default=None)
        if idx is None: continue
        for alt in G[s[idx]]:
            n=s[:idx]+alt.replace('ε','')+s[idx+1:]
            if len(n)<=maxlen: q.append(n)
    return sorted(out,key=lambda x:(len(x),x))
