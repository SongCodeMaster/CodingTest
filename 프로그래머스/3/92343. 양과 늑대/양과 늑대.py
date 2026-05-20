def solution(info, edges):

    tree = [[] for _ in range(len(info))]
    max_count = 0
    
    for u, v in edges:
        tree[u].append(v)
        
    def dfs(current_node, sheep, wolf, next_nodes):
        nonlocal max_count
        
        if info[current_node] == 0: 
            sheep += 1
        else:
            wolf += 1
        
        if wolf >= sheep:
            return
        
        max_count = max(max_count, sheep)
        
        available = next_nodes[:]
        available.remove(current_node)
        
        for next_available in tree[current_node]:
            available.append(next_available)
        
        for next in available:
            dfs(next, sheep, wolf, available)
    
    dfs(0,0,0,[0])
    
    return max_count