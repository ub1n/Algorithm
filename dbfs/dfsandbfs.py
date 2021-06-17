import sys
from collections import deque

n,m,v=list(map(int,(sys.stdin.readline().split())))
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,(sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
for i in range(len(graph)):
    graph[i]=sorted(graph[i])
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:  #현재노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited2[start]=True #현재 노드를 방문처리
    while queue:    #큐에서 하나의 원소를 뽑아 출력하기
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:  #아직 방문하지 않은 인접한 원소들을 큐에 삽입입
           if not visited2[i]:
                queue.append(i)
                visited2[i]=True

visited2=[False]*(n+1)
dfs(graph,v,visited)
print('')
bfs(graph,v,visited2)