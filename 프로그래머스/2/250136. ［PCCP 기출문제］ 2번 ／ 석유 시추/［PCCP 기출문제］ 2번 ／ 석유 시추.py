# land 순차적으로 순회하며 석유 발견시 탐색시작
# 덩어리 size 표기하고 열 정보까지 저장, 순회 종료시 열 정보에 해당하는 배열에 size값까지 추가
# 배열에서 max size 추출해오기

from collections import deque

def solution(land):
    col_len = len(land[0])
    row_len = len(land)
    
    col_answer = [0]*(col_len)
    visited = [[False]*(col_len) for _ in range(row_len)]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    
    for r in range(row_len):
        for c in range(col_len):
            if not visited[r][c] and land[r][c] == 1:
                q = deque()
                q.append((r,c))
                visited[r][c] = True
                dist = 1
                col_set = set()
                
                while q:
                    curr_r, curr_c = q.popleft()
                    col_set.add(curr_c)
                    
                    for i in range(4):
                        nr = dr[i] + curr_r
                        nc = dc[i] + curr_c
                        
                        if 0 <= nr < row_len and 0 <= nc < col_len:
                            if not visited[nr][nc] and land[nr][nc] == 1:
                                visited[nr][nc] = True
                                dist += 1
                                q.append((nr, nc))
                                
                for i in col_set:
                    col_answer[i] += dist
    
    result = max(col_answer)
    
    return result