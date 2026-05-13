def solution(n, computers):
    answer = 0
    visited = [False]*(n)
    
    def dfs(node):
        for next in range(n):
            if not visited[next] and computers[node][next] == 1:
                visited[next] = True
                dfs(next)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i) 
            count += 1
        
    return count