# 케빈 베이컨
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
mat = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    mat[i][i] = 0

# 인접행렬 구현
for _ in range(m):
    u, v = map(int,input().split())
    mat[u][v] = 1
    mat[v][u] = 1

# 플로이드워셜
for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            mat[s][e] = min(mat[s][e], mat[s][k] + mat[k][e])

# 1번이 가장 작다
min_bacon = sum(mat[1][1:])
result_person = 1

for i in range(2, n+1):
    bakon = sum(mat[i][1:])
    if bakon < min_bacon:
        min_bacon = bakon
        result_person = i

print(result_person)