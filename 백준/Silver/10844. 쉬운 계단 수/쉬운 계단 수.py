import sys
input = sys.stdin.readline
mod = 1000000000

n = int(input())

# dp테이블 생성
# 각 자리수마다 몇가지 가지치기가 가능한지 저장해둔다.
dp = [[0]*10 for _ in range(n + 1)]

# 1. 초기값 설정
for i in range(1, 10):
    dp[1][i] = 1 # 1, 2, ,..., 9는 각각 1개씩 존재

# 2. DP 진행 (N=2부터 N까지)
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            # 0은 1에서만 가능
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            # 9는 8에서만 가능
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % mod)