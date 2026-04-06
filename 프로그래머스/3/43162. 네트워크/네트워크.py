# 연결요소 개수 세기, dfs 몇번된건지?
def dfs(n, node, computers):
    global visited
    visited[node] = True
    
    for nxt in range(0,n):
        if not visited[nxt] and computers[node][nxt] == 1:
            dfs(n, nxt, computers)
    
def solution(n, computers):
    global visited
    visited = [False]*(n)
    count = 0
    
    for i in range(0,n):
            if not visited[i]:
                dfs(n, i, computers)
                count += 1
    
    return count