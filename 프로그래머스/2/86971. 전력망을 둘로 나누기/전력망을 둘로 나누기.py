def solution(n, wires):
    answer = 101
    
    tree = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)
        
    def dfs(node):
        nonlocal answer
        visited[node] = True
        
        my_tree_size = 1
        
        for next in tree[node]:
            if not visited[next]:
                child_size = dfs(next)
                
                diff = abs((child_size) - (n - child_size))
                answer = min(answer, diff)
                
                my_tree_size += child_size
                
        return my_tree_size
        
    dfs(1)
    
    return answer