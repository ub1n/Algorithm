import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

def bs(arr,n,start,end):
    mid=(start+end)//2
    if start>end:
        return None
    if arr[mid]==n:
        return 1
    elif arr[mid]>n:
        return bs(arr,n,start,mid-1)
    else:
        return bs(arr,n,mid+1,end)

a=sorted(a)
for i in b:
    if a.count(i)==0:
        print(0)
    else:
        print(1)