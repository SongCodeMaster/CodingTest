from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

# 2차원 배열 
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().strip())))

visited = [[False]*(N) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_x,start_y):
    #  큐 설정 및 이동 방향(상,하,좌,우)
    q = deque([(start_x, start_y)]) 
    visited[start_x][start_y] = True
    count = 1 # 단지 내 집의 개수 (현재 시작점 포함)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안이고, 갈 수 있는 경우
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    q.append((nx,ny))

    return count

# 단지별 집의 수
result = []
apart_count = 0
# 지도의 칸 하나씩 확인
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
            apart_count += 1

result.sort()

print(apart_count)
for i in range(len(result)):
    print(result[i])