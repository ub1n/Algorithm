from collections import deque
import copy
import sys


m,n=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    graph.append(a)
dx=[-1,1,0,0]   #이동할 네가지 방향 정의: 상,하.좌.우
dy=[0,0,-1,1]
graph2=copy.deepcopy(graph)
visited=[[False for _ in range(m)] for _ in range(n)]
def bfs():
    queue=deque()   #큐 구현을 위해 deque 라이브러리 사용
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))  #1인지점 먼저 큐에 담기
    while queue:    #큐가 빌때까지 반복하기
        x,y=queue.popleft()
        for i in range(4):  #현 위치에서 4가지 방향으로 위치확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:  #공간을 벗어난 경우 무시
                continue
            if graph2[nx][ny]==-1:    #벽인 경우 무시
                continue
            if graph[nx][ny]==0:    #해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[0][0]  #가장 오른쪽 아래까지의 최단거리 반환
bfs()
max=0
z=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            z=1
            break
        elif graph[i][j]>max:
            max=graph[i][j]
if z==1:
    print(-1)
else:
    print(max-1)