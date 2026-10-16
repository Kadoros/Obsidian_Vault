import re
CODES={'(':25,')':26,'+':21,'-':22,'*':23,'/':24,'=':20}
def lexs(s):
    out=[]
    for m in re.finditer(r'[A-Za-z][A-Za-z0-9]*|\d+|\S',s):
        t=m.group()
        if t[0].isalpha(): out.append((11,t))
        elif t[0].isdigit(): out.append((10,t))
        else: out.append((CODES.get(t,99),t))
    out.append((-1,'EOF')); return out
def trace(s):
    toks=lexs(s); i=[0]; L=[]
    def lex():
        c,t=toks[i[0]]; i[0]+=1; L.append(f'Next token is: {c} Next lexeme is {t}'); return c
    nt=[lex()]
    def expr():
        L.append('Enter <expr>'); term()
        while nt[0] in (21,22): nt[0]=lex(); term()
        L.append('Exit <expr>')
    def term():
        L.append('Enter <term>'); factor()
        while nt[0] in (23,24): nt[0]=lex(); factor()
        L.append('Exit <term>')
    def factor():
        L.append('Enter <factor>')
        if nt[0] in (10,11): nt[0]=lex()
        elif nt[0]==25:
            nt[0]=lex(); expr()
            if nt[0]==26: nt[0]=lex()
            else: L.append('ERROR')
        else: L.append('ERROR')
        L.append('Exit <factor>')
    expr(); return L
import sys
for s in sys.argv[1:]:
    print('==',s); print('\n'.join(trace(s)))
