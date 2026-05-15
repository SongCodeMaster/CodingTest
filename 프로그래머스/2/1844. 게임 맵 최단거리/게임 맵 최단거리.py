from collections import deque
# 방향벡터 정의후 연결된 요소끼리 이동하며 dist return
def solution(maps):
    answer = 0
    row_len = len(maps)
    col_len = len(maps[0])
    
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    
    visited = [[False]*(col_len) for _ in range(row_len)]
    
    def bfs(start_row, start_col):
        q = deque()
        q.append((start_row, start_col, 1))
        visited[start_row][start_col] = True
        while q:
            current_row, current_col, dist = q.popleft()
            
            if current_row == (row_len - 1) and current_col == (col_len - 1):
                return dist
            for i in range(4):
                next_row = dr[i] + current_row
                next_col = dc[i] + current_col
                
                if 0 <= next_row < row_len and 0 <= next_col < col_len and maps[next_row][next_col] == 1:
                    if not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        q.append((next_row, next_col, dist + 1))
        
        return -1
    
    return bfs(0,0)
     