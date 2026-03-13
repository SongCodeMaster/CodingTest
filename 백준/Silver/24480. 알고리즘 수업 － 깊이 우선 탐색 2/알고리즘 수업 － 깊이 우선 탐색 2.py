import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, start = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 내림차순
for i in range(1,N+1):
    arr[i].sort(reverse=True)

visited = [0]*(N+1)
count = 0

def dfs(node):
    global count
    count += 1
    visited[node] = count

    for i in arr[node]:
        if visited[i] == 0:
            dfs(i)

dfs(start)

print('\n'.join(map(str,visited[1:])))