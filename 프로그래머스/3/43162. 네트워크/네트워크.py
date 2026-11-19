# dfs로 연결요소 개수 세기
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        for nxt in range(n):
            if not visited[nxt] and computers[node][nxt] == 1:
                visited[nxt] = True
                dfs(nxt)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    
    return answer