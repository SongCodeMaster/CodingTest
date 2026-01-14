# 방향O 최단거리 가면서 출력해라. 
# BFS 활용하면 되겠음.
# 최단거리 저장해두고 출력하기.
import sys
from collections import deque
input = sys.stdin.readline

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())

# 노드 생성
graph = [[] for _ in range(N+1)]

# 간선 연결
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# BFS 구현
visited = [False]*(N+1)
distance = [0] * (N+1)

def bfs(start,k):
    res = [] # 출력용
    visited[start] = True
    q = deque([start])

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                distance[nxt] = distance[v] + 1 # 처음 x 기준으로 거리 체크
                if distance[nxt] == k: 
                    res.append(nxt) # 거리 발견시 출력 리스트에 추가
    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i])

bfs(X, K)