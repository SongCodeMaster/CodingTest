from collections import deque
# 예외케이스: 도달못하면 return -1, 최솟값 return, BFS
def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    visited = [[False] * (col) for _ in range(row)]
    
    q = deque()
    visited[0][0] = True
    q.append((0,0,1))
    dist = 0
    
    while q:
        start_r, start_c, dist = q.popleft()
        
        if start_r == row - 1 and start_c == col - 1:
            return dist
        
        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]
            
            if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == False and maps[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr,nc,dist+1))
    
    return -1