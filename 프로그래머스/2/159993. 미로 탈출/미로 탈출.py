from collections import deque

def solution(maps):
    result = 0
    len_r = len(maps)
    len_c = len(maps[0])
    start_r, start_c = 0, 0
    lever_r, lever_c = 0, 0
    end_r, end_c = 0, 0
    
    dr = [-1,1,0,0] 
    dc = [0,0,-1,1]
    for i in range(len_r):
        for j in range(len_c):
            if maps[i][j] == "S":
                start_r, start_c = i, j
            elif maps[i][j] == "L":
                lever_r, lever_c = i, j
            elif maps[i][j] == "E":
                end_r, end_c = i,j 
    
    def bfs(s_r, s_c, e_r, e_c):
        visited = [[False]*len_c for _ in range(len_r)]
        q = deque()
        q.append((s_r, s_c, 0))
        visited[s_r][s_c] = True
        
        while q:
            cur_r, cur_c, dist = q.popleft()
            
            if cur_r == e_r and cur_c == e_c:
                return dist
            
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if 0 <= next_r < len_r and 0 <= next_c < len_c and maps[next_r][next_c] != "X":
                    if not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        q.append((next_r, next_c, dist + 1))
        
        return -1
    
    lever_distance = bfs(start_r, start_c, lever_r, lever_c)
    if lever_distance == -1:
        return -1
        
    end_distance = bfs(lever_r, lever_c, end_r, end_c)
    if end_distance == -1:
        return -1
        

    result = lever_distance + end_distance
        
    return result