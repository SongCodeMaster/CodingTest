from collections import deque
def solution(n, edge):
    answer = 0
    visited = [True] * (n+1)
    
    graph = [[] for _ in range(n+1) ]
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    distance = [0]*(n+1)
    
    q = deque()
    q.append(1)
    
    while q:
        curr_node = q.popleft()
        
        for next_node in graph[curr_node]:
            if distance[next_node] == 0 and next_node != 1:
                distance[next_node] += 1 + distance[curr_node]
                q.append(next_node)
    
    max_value = max(distance)
    
    for i in range(n+1):
        if distance[i] == max_value:
            answer += 1
    print(distance)
    return answer