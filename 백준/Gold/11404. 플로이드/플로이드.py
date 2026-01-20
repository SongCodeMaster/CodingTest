# 플로이드 워셜: 인접행렬, 삼중for문 + min()으로계산
import sys

n = int(input())
m = int(input())

# 인접행렬초기화
INF = sys.maxsize
mat = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    mat[i][i] = 0

for _ in range(m):
    u, v, w = map(int,input().split())
    if w < mat[u][v]:
        mat[u][v] = w

# 플로이드 워셜 구현
for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            mat[s][e] = min(mat[s][e], mat[s][k] + mat[k][e])

for i in range(1,n+1):
    for j in range(1, n+1):
        if mat[i][j] == INF:
            print(0, end=' ')
        else:
            print(mat[i][j],end=' ')
        if j == n:
            print()