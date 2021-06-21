import sys

n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
result=0
def dfs(x,y):
    if x<= -1 or x>=n or y<= -1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        global result
        result+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
answer=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            answer.append(result)
            result=0
answer=sorted(answer)
print(len(answer))
for i in answer:
    print(i)