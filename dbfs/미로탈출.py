from collections import deque

def bfs(x,y):
    queue=deque()   #큐 구현을 위해 deque 라이브러리 사용
    queue.append((x,y))
    while queue:    #큐가 빌때까지 반복하기
        x,y=queue.popleft()
        for i in range(4):  #현 위치에서 4가지 방향으로 위치확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:  #미로 공간을 벗어난 경우 무시
                continue
            if graph[nx][ny]==0:    #벽인 경우 무시
                continue
            if graph[nx][ny]==1:    #해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]  #가장 오른쪽 아래까지의 최단거리 반환

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]   #이동할 네가지 방향 정의: 상,하.좌.우
dy=[0,0,-1,1]

print(bfs(0,0))