import sys
# 재귀함수 런타임 오류 방지
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# dfs 함수 만들기
def dfs(node):
    visited[node] = True
    for next_node in arr[node]:
        if visited[next_node] == False:
            dfs(next_node)


cnt = 0
visited = [False] * (N + 1)
for n in range(1, N+1):
    if not visited[n]:
        dfs(n)
        cnt += 1

print(cnt)