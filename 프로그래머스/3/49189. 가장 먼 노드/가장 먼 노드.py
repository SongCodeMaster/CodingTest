# bfs로 이동했을때 간선의 개수가 가장 많은 것 (가중치)
# 가장 멀리 떨어진 노드가 몇개인지 return 가중치 3인것들 배열에 저장해놨다가 빼두기?
from collections import deque
def solution(n, edge):
    answer = 0
    visited = [False] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    distance = [0] * (n+1)

    q = deque()
    q.append(1)
    visited[1] = True
    
    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                distance[nxt] = distance[curr] + 1
                q.append(nxt)
    
    my_ans = max(distance)
    
    for k in distance:
        if k == my_ans:
            answer += 1
            
    return answer