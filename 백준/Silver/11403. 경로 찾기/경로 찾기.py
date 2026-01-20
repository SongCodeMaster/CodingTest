# 인접행렬 문제이다. 간선이 무방향으로 존재하며 자기자신으로 방문가능하면 1
# 모든 노드 전수 탐색해야하기 때문에 플로이드
n = int(input())

mat = [[0]*n for _ in range(n)]

for i in range(n):
    v = list(map(int,input().split()))
    for j in range(len(v)):
        if v[j] == 1:
            mat[i][j] = 1

# 플로이드워셜 구현
for k in range(n):
    for i in range(n):
        for j in range(n):
            if mat[i][k] == 1 and mat[k][j] == 1:
                mat[i][j] = 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()