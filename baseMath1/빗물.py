import sys

h,w=map(int,sys.stdin.readline().split())
block=list(map(int,sys.stdin.readline().split()))
left=[]
left.append(block[0])
left.append(0)
right=[]
right.append(block[1])
right.append(1)
answer=0
for i in range(1,w-1):
    if left<=right:
        left[0]=block[i]
        left[1]=i
        right[0]=block[i+1]
        right[1]=i+1
    else:
        if right[0]<block[i+1]:
            m=min(left[0],block[i+1])
            for j in range(left[1]+1,i+1):
                if m-block[j]>0:
                    answer+=m-block[j]
                    block[j]=m
            right[0]=block[i+1]
            right[1]=i+1
        else:
            right[0]=block[i+1]
            right[1]=i+1
print(answer)