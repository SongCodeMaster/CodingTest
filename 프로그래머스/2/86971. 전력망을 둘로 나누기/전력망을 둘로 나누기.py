# 후위순회하며 서브트리 값 최솟값 갱신 비교
def solution(n, wires):
    answer = 101
    visited = [False] * (n+1)
    tree = [[] for _ in range(n+1)]
    
    for u,v in wires:
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
                
                answer = min(diff, answer)
                
                my_tree_size += child_size
                
        return my_tree_size
    
    dfs(1)
    return answer