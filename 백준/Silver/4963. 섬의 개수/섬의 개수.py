import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,e):
    q = deque()
    q.append((s,e))
    visited[e][s] = True

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < u and 0 <= ny < v:
                if mat[ny][nx] == 1 and not visited[ny][nx]:
                    q.append((nx,ny))
                    visited[ny][nx] = True

while True:
    
    u, v = map(int, input().split())
    
    if u == 0 and v == 0:
        sys.exit()
        
    mat = []

    for _ in range(v):
        arr = list(map(int, input().split()))
        mat.append(arr)

    dx = [-1,1,0,0,1,-1,-1,1]
    dy = [0,0,-1,1,1,1,-1,-1]

    # mat 순회(조건: not visit, 1)하면서 bfs()호출

    visited = [[False]*(u) for _ in range(v)]

    count = 0
    for i in range(u):
        for j in range(v):
            if mat[j][i] == 1 and not visited[j][i]:
                bfs(i,j)
                count += 1

    print(count)