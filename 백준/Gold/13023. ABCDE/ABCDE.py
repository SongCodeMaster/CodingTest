import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [False] * N
found = False

for i in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node, depth):
    global found
    if found:
        return
    if depth == 5: # 사람 5명 연결됨 간선 4개
        found = True
        return
    
    visited[node] = True
    for next_node in arr[node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)

    visited[node] = False # 백트래킹: 다른 경로 탐색 위해 복구

for n in range(0,N):
    dfs(n, 1)
    if found:
        break

print(1 if found else 0)