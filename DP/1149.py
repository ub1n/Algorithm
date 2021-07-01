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
    for i in range(3):
        if i==0: #첫번쨰 페인트 이전에 고를경우
            one=dp[j-1][1]
            two=dp[j-1][2]
        elif i==1:
            one=dp[j-1][0]
            two=dp[j-1][2]
        elif i==2:
            one=dp[j-1][0]
            two=dp[j-1][1]
        dp[j][i]=dp[j][i]+min(one,two)
result=dp[n-1][0]
for i in range(3):
    result=min(result,dp[n-1][i])
print(result)
