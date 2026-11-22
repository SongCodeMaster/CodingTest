from collections import deque

# 레버 최소거리 이동 + 레버부터 도착지점 최소거리 이동
def solution(maps):
    
    row_len = len(maps)
    col_len = len(maps[0])
    
    start_r, start_c = 0, 0
    lever_r, lever_c = 0, 0
    end_r, end_c = 0,0
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    # 좌표 찾기
    for i in range(row_len):
        for j in range(col_len):
            if maps[i][j] == 'S':
                start_r, start_c = i, j
            if maps[i][j] == 'L':
                lever_r, lever_c = i, j
            if maps[i][j] == 'E':
                end_r, end_c = i, j
    
    
    
    def bfs(s_r, s_c, e_r, e_c):
        visited = [[False]*(col_len) for _ in range(row_len)]
        visited[s_r][s_c] = True
        
        q = deque()
        dist = 0
        q.append((s_r, s_c, dist))
        
        while q:
            curr_r, curr_c, dist = q.popleft()
            
            if curr_r == e_r and curr_c == e_c:
                return dist
            
            for i in range(4):
                nr = dr[i] + curr_r
                nc = dc[i] + curr_c
                if 0 <= nr < row_len  and 0 <= nc < col_len:
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc, dist+1))
        return -1
                    
    start_to_lever = bfs(start_r, start_c, lever_r, lever_c)
    lever_to_end = bfs(lever_r, lever_c, end_r, end_c)
    
    if start_to_lever == -1 or lever_to_end == -1:
        return -1 
    
    return start_to_lever + lever_to_end