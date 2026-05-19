# 연결되어있는 그래프에서 간선 하나를 끊었을때의 네트워크
# 전력망 크기 차이 = abs(서브트리 크기 - (n - 서브트리 크기))
def solution(n, wires):
    answer = 102
    tree = [[] for _ in range(n+1)]
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)
    
    visited = [False]*(n+1)
    
    def dfs(node):
        nonlocal answer
        visited[node] = True
        subtree_size = 1 # 서브트리
        
        for next in tree[node]:
            if not visited[next]:
                # 자식 서브트리 구해오기
                child_size = dfs(next)
                
                diff = abs(child_size - (n-child_size))
                answer = min(answer, diff) # 최솟값 갱신
                
                subtree_size += child_size
                
        return subtree_size
    
    dfs(1)
    
    return answer