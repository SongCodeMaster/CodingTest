# 연산의 최솟값
# 큰 문제를 작은문제로 나누는게 가능 -> 10에서 -1후 9의 최소해
# 자연수에서 1을뺀후 최소 연산값 vs 자연수에서 그대로 나눈후의 연산값
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1] = 0

for i in range(2,n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[n])