import sys

n=int(sys.stdin.readline())
array=[]
for i in range(n):
    m=list(map(int,sys.stdin.readline().split()))
    array.append(m)
dp=[]
index=0
for i in range(n):
    dp.append(array[i])

for j in range(1,n):
    for i in range(j+1):
        if i==0: #첫번쨰 페인트 이전에 고를경우
            left=-1
            right=dp[j-1][0]
        elif i==j:
            left=dp[j-1][i-1]
            right=-1
        else:
            left=dp[j-1][i-1]
            right=dp[j-1][i]
        dp[j][i]=dp[j][i]+max(left,right)
result=0
for i in range(n):
    result=max(result,dp[n-1][i])
print(result)