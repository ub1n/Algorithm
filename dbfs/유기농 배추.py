import sys

sys.setrecursionlimit(10000)
t=int(sys.stdin.readline())

for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    graph=[[0 for col in range(m)] for row in range(n)]  #[가로] for 세로
    for j in range(k):
        a,b=map(int,sys.stdin.readline().split())
        graph[b][a]=1

    def dfs(x, y):  #DFS로 특정 노드를 방문하고 연결된 모드 노드들도 방문
        if x <= -1 or x >= n or y <= -1 or y >= m:  #주어진 범위를 벗어나는 경우 즉시 종료
            return False
        if graph[x][y] == 1:    #현재 노드를 아직 방문하지않았다면
            graph[x][y] = 0     #해당노드 방문처리
            dfs(x - 1, y)       #상,하,좌,우 재귀적으로 호출
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    result=0
    for i in range(n):      #모든 노드에 대해 채우기
        for j in range(m):
            if dfs(i, j) == True:   #현 위치에서 DFS 수행
                result+=1
    print(result)

