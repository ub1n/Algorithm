from collections import deque
import sys


m,n,h=map(int,sys.stdin.readline().split())
graph=[]
for i in range(h):
    b=[]
    for j in range(n):
        a=list(map(int,sys.stdin.readline().split()))
        b.append(a)
    graph.append(b)
dx=[-1,1,0,0,0,0]   #이동할 네가지 방향 정의: 상,하.좌.우
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
def bfs():
    queue=deque()   #큐 구현을 위해 deque 라이브러리 사용
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==1:
                    queue.append((i,j,k))
    while queue:    #큐가 빌때까지 반복하기
        q=queue.popleft()
        for i in range(6):  #현 위치에서 4가지 방향으로 위치확인
            nx=q[1]+dx[i]
            ny=q[2]+dy[i]
            nz=q[0]+dz[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or nz<0 or nz>=h:  #공간을 벗어난 경우 무시
                continue
            if graph[nz][nx][ny]==-1:    #벽인 경우 무시
                continue
            if graph[nz][nx][ny]==0:    #해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nz][nx][ny]=graph[q[0]][q[1]][q[2]]+1
                queue.append((nz,nx,ny))
    return graph[0][0][0]  #가장 오른쪽 아래까지의 최단거리 반환
bfs()
max=0
z=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                z=1
                break
            elif graph[i][j][k]>max:
                max=graph[i][j][k]
if z==1:
    print(-1)
else:
    print(max-1)