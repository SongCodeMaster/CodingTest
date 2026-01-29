import sys
input = sys.stdin.readline

n = int(input())
T = [0]*(n + 1) # 걸리는 시간
A = [0]*(n + 1) # 이익

# 배열 받기
for i in range(1,n+1):
    x, y = map(int,input().split())
    T[i] = x
    A[i] = y

dp = [0]*(n + 2)
# DP 풀이: i일의 최대의 수익
for i in range(n,0,-1):
    if i + T[i] <= n+1:
        dp[i] = max(dp[i+1], A[i]+ dp[i + T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[1])
