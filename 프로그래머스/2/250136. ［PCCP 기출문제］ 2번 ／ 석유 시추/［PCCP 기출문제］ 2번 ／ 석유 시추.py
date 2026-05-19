from collections import deque
def solution(land):
    row_len = len(land)
    col_len = len(land[0])
    
    # 각 열별로 획득가능한 석유의 총량을 저장할 배열
    result_col = [0] * col_len
    
    visited = [[False]*(col_len) for _ in range(row_len)]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    # 전체 땅 순회
    for r in range(row_len):
        for c in range(col_len):
            # 석유 O, 방문 X = 탐색시작
            if land[r][c] == 1 and not visited[r][c]:
                q = deque([(r, c)])
                visited[r][c] = True
                
                chunk_size = 0 # 석유 크기
                cols_hit = set() # 이번 덩어리 열 저장하기(중복제거)
                
                while q:
                    current_r, current_c = q.popleft()
                    chunk_size += 1
                    cols_hit.add(current_c)
                    
                    for i in range(4):
                        nr = current_r + dr[i]
                        nc = current_c + dc[i]
                        
                        if 0 <= nr < row_len and 0 <= nc < col_len:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr,nc))
                        
                # bfs 끝나면, 덩어리가 걸친 모든 열에 석유 크기 누적합해준다.
                for cols in cols_hit:
                    result_col[cols] += chunk_size
    
    # 누적합에서 최댓값 뽑아서 return
    result = max(result_col)
    return result
                        
                        