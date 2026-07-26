from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distances = [-1] * (n + 1)
    distances[1] = 0
    q = deque([1])
    
    while q:
        curr = q.popleft()
        
        for nxt in graph[curr]:
            if distances[nxt] == -1:
                distances[nxt] = distances[curr] + 1
                q.append(nxt)
                
    max_dist = max(distances)
    return distances.count(max_dist)