import sys

n=list(map(int,sys.stdin.readline().split()))
arr=[]
for i in range(n[0]):
    m=int(sys.stdin.readline())
    arr.append(m)
start=1
end=max(arr)
ans=[]
while(start<=end):
    mid=(start+end)//2
    temp=sum([i//mid for i in arr])
    if temp>=n[1]:
        ans.append(mid)
        start=mid+1
    else:
        end=mid-1
print(max(ans))