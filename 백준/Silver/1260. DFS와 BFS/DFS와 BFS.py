from collections import deque
import sys
sys.setrecursionlimit(10000)

N, M, start = list(map(int, input().split()))
arr = [[] for _ in range(N+1)]

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

visited = [False] * (N+1)

dfs(start)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in arr[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()

visited = [False] * (N+1)
bfs(start)
