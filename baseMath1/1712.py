import sys

k=int(sys.stdin.readline())
apt=[]
a=[]
for i in range(15):
    a.append(i)
apt.append(a)
for i in range(1,15):
    a=[]
    for j in range(15):
        b=apt[i-1][:j+1]
        a.append(sum(b))
    apt.append(a)
for i in range(k):
    n=int(sys.stdin.readline())
    m=int(sys.stdin.readline())
    print(apt[n][m])


