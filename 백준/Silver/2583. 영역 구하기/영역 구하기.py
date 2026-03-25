import sys
from collections import deque
input = sys.stdin.readline

# M: 행 N: 열
M, N, K = map(int, input().split())

mat = [ [0]*(N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            mat[y][x] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy,sx):

    q = deque()
    q.append((sy,sx))
    box_count = 1
    visited[sy][sx] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx
            if 0 <= ny < M and 0 <= nx < N:
                if not visited[ny][nx] and mat[ny][nx] == 0:
                    visited[ny][nx] = True
                    box_count += 1
                    q.append((ny,nx))

    result.append(box_count)

visited = [[False]*(N) for _ in range(M)]

count = 0
result = []
for y in range(M):
    for x in range(N):
        if mat[y][x] == 0 and not visited[y][x]:
            bfs(y,x)
            count += 1

print(count)
result.sort()
print(*result)