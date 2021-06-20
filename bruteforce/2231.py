
import sys

n = int(sys.stdin.readline())
man = []
dic={}

for i in range(n):
    s = sys.stdin.readline().split()
    s.append(i)
    man.append(s)
ans=[]
for i in range(n):
    temp=1
    for j in range(n):
        if i==j:
            continue
        if int(man[i][0])<int(man[j][0]) and int(man[i][1])<int(man[j][1]):
            temp+=1
    ans.append(temp)
answer=''
for i in range(len(ans)):
    if i==len(ans)-1:
        answer+=str(ans[i])
    else:
        answer+=str(ans[i])+' '
print(answer)
# def compare(x, y):
#     if x[0] < y[0] and x[1] < y[1]:
#         return -1
#     else:
#         return 1
#
# sot=sorted(man,key=cmp_to_key(compare),reverse=True)
# answer=[-1]*n
# temp=1
# for i in range(n):
#     if i!=0:
#         if sot[i][1]<sot[i-1][1] and sot[i][0]<sot[i-1][0]:
#             temp=i+1
#     answer[sot[i][2]]=temp
# print(answer)