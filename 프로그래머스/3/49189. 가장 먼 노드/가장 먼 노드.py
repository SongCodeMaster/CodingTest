from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for i in range(len(edge)):
        j,k = edge[i]
        graph[j].append(k)
        graph[k].append(j)
    
    distance = [-1]*(n+1)
    
    def bfs(node):
        q = deque()
        q.append(node)
        distance[node] += 1
        
        while q:
            current_node = q.popleft()
            
            for next in graph[current_node]:
                if distance[next] == -1:
                    distance[next] = distance[current_node] + 1
                    q.append(next)
        
    bfs(1)
    max_result = max(distance)
    
    count = 0
    for i in range(n+1):
        if distance[i] == max_result:
            count += 1
    return count