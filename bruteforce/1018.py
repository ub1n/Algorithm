import sys

mn = sys.stdin.readline().split()
n=int(mn[0])
m=int(mn[1])
col=[]
wChess=[]
bChess=[]
for i in range(8):
    if i%2==0:
        wChess.append('WBWBWBWB')
        bChess.append('BWBWBWBW')
    else:
        wChess.append('BWBWBWBW')
        bChess.append('WBWBWBWB')
for i in range(n):
    a = sys.stdin.readline().split()
    col.append(a)
ans=[]
for i in range(m):
    if i+8>m:
        continue
    for j in range(n):
        if j+8>n:
            continue
        #j 세로 i 가로 col[j][i]
        chess=[]
        if col[j][0][i]=='W':
            chess=wChess
        else:
            chess=bChess
        wcnt=0
        bcnt=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if wChess[b - j][a - i] != col[b][0][a]:
                    wcnt += 1
                if bChess[b-j][a-i]!=col[b][0][a]:
                    bcnt+=1
        tem=[]
        tem.append(i)
        tem.append(j)
        if wcnt>bcnt:
            tem.append(bcnt)
        else:
            tem.append(wcnt)
        ans.append(tem)
ans=sorted(ans,key=lambda x:x[2])
print(ans[0][2])


