def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for next in range(n):
            if not visited[next] and computers[node][next] == 1:
                dfs(next)
                
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count 