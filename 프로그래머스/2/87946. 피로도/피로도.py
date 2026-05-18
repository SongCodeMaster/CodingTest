def solution(k, dungeons):
    max_dungeons = 0
    visited = [False] * (len(dungeons))
    
    def dfs(current_k, count):
        nonlocal max_dungeons
        
        # 현재까지 탐험한 던전 수(count)로 최댓값 갱신
        max_dungeons = max(max_dungeons, count)
        
        # 순열 탐색 (항상 0번 던전부터 확인하되, 안 간 곳만 감)
        for i in range(len(dungeons)):
            # 1. 아직 방문하지 않았고
            # 2. 현재 피로도가 해당 던전의 '최소 필요 피로도'보다 크거나 같다면
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                
                # 다음 재귀 호출: 피로도 깎기, 던전 탐험 횟수 1 늘리기
                dfs(current_k - dungeons[i][1], count + 1)
                
                visited[i] = False # 상태 복구 (backTrack)
    
    dfs(k, 0)
    
    return max_dungeons