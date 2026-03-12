import sys
# 재귀 깊이 설정 (필요 시 더 늘릴 수 있음)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

# 인접 리스트 구성
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 오름차순 방문을 위한 정렬
for i in range(1, n + 1):
    arr[i].sort()

# visited에 방문 순서를 기록 (0으로 초기화)
visited = [0] * (n + 1)
count = 1

def dfs(curr):
    global count
    visited[curr] = count  # 현재 노드에 방문 순서 기록
    
    for neighbor in arr[curr]:
        if visited[neighbor] == 0: # 아직 방문하지 않았다면
            count += 1
            dfs(neighbor)

# DFS 시작
dfs(r)

# 1번부터 n번 노드까지의 방문 순서를 출력
# 방문하지 못한 곳은 초기값인 0이 그대로 출력됨
print('\n'.join(map(str, visited[1:])))