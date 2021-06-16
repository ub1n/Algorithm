import sys

n = int(sys.stdin.readline())
temp=665
cnt=0
while True:
    s=str(temp)
    if s.find('666')!=-1:
        cnt+=1
    if cnt==n:
        break
    temp+=1

print(temp)