import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 그래프 입력
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

# DFS
def dfs(n):
    global count
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            count += 1
            dfs(i)

visited = [False] * (n+1)
dfs(1)
print(count)