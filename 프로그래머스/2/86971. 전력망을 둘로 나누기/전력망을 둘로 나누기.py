# 트리에서 서브트리 빼면서 최솟값 갱신
def solution(n, wires):
    answer = 100
    
    visited = [False] * (n+1)
    tree = [[] for _ in range(n+1)]
    
    for u, v in wires :
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node):
        nonlocal answer 
        visited[node] = True
        subtree_size = 1
        for next in tree[node]:
            if not visited[next]:
                child_size = dfs(next)
                diff = abs(child_size - (n-child_size))
                
                answer = min(answer, diff)
                subtree_size += child_size
                
        return subtree_size
    dfs(1)
        
    return answer