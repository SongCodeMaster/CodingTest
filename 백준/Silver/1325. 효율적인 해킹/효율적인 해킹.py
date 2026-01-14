# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 찾기
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[]for _ in range(N+1)]

# 간선 연결
for _ in range(M):
    u, v = map(int, input().split())
    graph[v].append(u) # 방향존재

# bfs
def bfs(v):
    cnt = 1
    visited=[False]*(N+1)
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

result = []
for i in range(1, N+1):
    result.append(bfs(i))

m = max(result)
for i in range(len(result)):
    if m == result[i]:
        print(i+1, end=' ')