import sys

n=list(map(int,sys.stdin.readline().split()))
a=list(map(int,sys.stdin.readline().split()))
start=0
end=max(a)
ans=[]
while(start<=end):
    mid=(start+end)//2
    temp=sum([i-mid if mid<i else 0 for i in a])
    if temp>=n[1]:
        ans.append(mid)
        start=mid+1
    else:
        end=mid-1
print(max(ans))