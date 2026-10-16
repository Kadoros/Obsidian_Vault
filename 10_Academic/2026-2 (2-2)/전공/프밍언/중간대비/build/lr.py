R={1:('E',3),2:('E',1),3:('T',3),4:('T',1),5:('F',3),6:('F',1)}
RS={1:'E→E+T',2:'E→T',3:'T→T*F',4:'T→F',5:'F→(E)',6:'F→id'}
A={0:{'id':'S5','(':'S4'},1:{'+':'S6','$':'acc'},2:{'+':'R2','*':'S7',')':'R2','$':'R2'},3:{'+':'R4','*':'R4',')':'R4','$':'R4'},
4:{'id':'S5','(':'S4'},5:{'+':'R6','*':'R6',')':'R6','$':'R6'},6:{'id':'S5','(':'S4'},7:{'id':'S5','(':'S4'},8:{'+':'S6',')':'S11'},
9:{'+':'R1','*':'S7',')':'R1','$':'R1'},10:{'+':'R3','*':'R3',')':'R3','$':'R3'},11:{'+':'R5','*':'R5',')':'R5','$':'R5'}}
G={0:{'E':1,'T':2,'F':3},4:{'E':8,'T':2,'F':3},6:{'T':9,'F':3},7:{'F':10}}
def run(s):
    toks=s.split()+['$']; st=[0]; i=0; out=[]
    while True:
        stack=''.join(str(x) for x in st); inp=' '.join(toks[i:])
        a=A[st[-1]].get(toks[i])
        if a is None: out.append((stack,inp,'ERROR')); break
        if a=='acc': out.append((stack,inp,'accept')); break
        if a[0]=='S':
            out.append((stack,inp,f'Shift {a[1:]}')); st+= [toks[i],int(a[1:])]; i+=1
        else:
            r=int(a[1:]); l,n=R[r]; st=st[:len(st)-2*n]; g=G[st[-1]][l]
            out.append((stack,inp,f'Reduce {r} ({RS[r]}), goto[{st[-1]},{l}]={g}')); st+=[l,g]
    return out
import sys
for s in sys.argv[1:]:
    print('==',s)
    for r in run(s): print(f'{r[0]:<22} | {r[1]:<22} | {r[2]}')
