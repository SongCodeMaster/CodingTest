from collections import deque
N, M, start = list(map(int, input().split()))
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N+1):
    arr[i].sort()

def dfs(v):
    print(v, end= ' ')
    visited[v]=True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)



def bfs(graph, start):
    visited = set([start]) # 현재노드 방문
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for nxt in graph[vertex]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

dfs(start)
print()
bfs(arr, start)
