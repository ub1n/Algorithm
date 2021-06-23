import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,(sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
answer=0
visited=[False]*(n+1)
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:  #현재노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            global answer
            answer+=1
            dfs(graph,i,visited)
dfs(graph,1,visited)
print(answer)