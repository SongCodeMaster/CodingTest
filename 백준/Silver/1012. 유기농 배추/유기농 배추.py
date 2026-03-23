from collections import deque
import sys
input = sys.stdin.readline
# 연결요소 개수 세기 문제
T = int(input()) # 이따가 생각

while T > 0:
    M, N, K = map(int, input().split())

    mat = [[0]*(M) for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1
        
    visited = [[False]*(M) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(start_x, start_y):
        q = deque()
        q.append((start_x, start_y))
        visited[start_y][start_x] = True

        while q:
            x, y = q.popleft()
            
            for i in range(4):
                next_x = dx[i] + x
                next_y = dy[i] + y
                if 0 <= next_x < M and 0 <= next_y < N:
                    if mat[next_y][next_x] == 1 and not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        q.append((next_x,next_y))

    count = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1 and not visited[i][j]:
                bfs(j,i)
                count += 1

    print(count)
    T -= 1