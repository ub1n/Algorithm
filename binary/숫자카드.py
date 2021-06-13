import sys
from bisect import bisect_right,bisect_left

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

a=sorted(a)
ans=''
for i in b:
    print(bisect_right(a,i)-bisect_left(a,i),end=' ')
print(ans)