import sys

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    zero=[]
    one=[]
    zero.append(1)
    zero.append(0)
    one.append(0)
    one.append(1)
    for j in range(2,n+1):
        z=one[j-1]
        o=zero[j-1]+one[j-1]
        zero.append(z)
        one.append(o)
    s=str(zero[n])+" "+str(one[n])
    print(s)
