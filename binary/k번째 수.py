import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())

a=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        a.append(i*j)
print(a[k])