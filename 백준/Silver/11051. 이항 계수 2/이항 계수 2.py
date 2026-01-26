# 조합구하는문제
# 점화식으로 풀이 (DP = 미리 계산하자)
# 2차원 행렬 초기화 -> 점화식 세워서 배열 채우기
import sys
input = sys.stdin.readline
mod = 10007 
n, k = map(int, input().split())

# 2차원 배열 생성
D = [ [0]*(n+1) for _ in range(n+1)]

# 기본값 설정
for i in range(1,n+1):
    D[i][i] = 1
    D[i][0] = 1
    D[i][1] = i

# 점화식 D[i][k] = D[i-1][k-1] + D[i-1][k]
for i in range(2, n+1):
    for j in range(1,i):
        D[i][j] = (D[i-1][j-1] + D[i-1][j]) % mod

print(D[n][k])