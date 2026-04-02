from collections import deque

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def bfs(n,m,maps,h,w,visited):
    visited[n][m] = 1
    q = deque()
    q.append((n,m))
    
    while q:
        u, v = q.popleft()
        
        if u == h-1 and v == w-1:
            return visited[u][v]
            
        for i in range(4):
            ny = dy[i] + u
            nx = dx[i] + v
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = visited[u][v] + 1
                    q.append((ny,nx))
    return -1

def solution(maps):

    h = len(maps)
    w = len(maps[0])
    
    visited = [[0]*(w) for _ in range(h)]
    
    return bfs(0,0,maps,h,w,visited)
    