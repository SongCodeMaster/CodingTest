
from collections import deque

# 입력받기 미로문제 그래프 표현
n, m = map(int, input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input())))

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 미로 탐색 구현
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i] # x 방향 이동한 곳
            ny = y + dy[i] # y 방향 이동한 곳
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1: # 그래프의 위치가 1이면
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))