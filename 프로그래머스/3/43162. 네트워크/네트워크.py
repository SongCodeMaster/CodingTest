def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    
    def dfs(curr_node):
        visited[curr_node] = True
        
        for i in range(n):
                if curr_node != i and computers[curr_node][i] == 1 and not visited[i]:
                    dfs(i)
                    
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
            
        
    return answer