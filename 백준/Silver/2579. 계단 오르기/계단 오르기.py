import sys
# 계단오르기
# 연속세자리 나오면 X, 
# max로 값비교 뭘로하고 DP에 뭘 저장할지
# 큰문제를 작은문제로 해결해야한다.

n = int(input())

A = [0]*(n+1)
for i in range(1, n+1):
    A[i] = int(input())

dp = [0]*(n+1)
dp[1] = A[1] 
if n == 1:
    print(dp[1])
    sys.exit()

dp[2] = A[1] + A[2]

for i in range(3,n+1):
    # 마지막에서 2칸 이동한 경우 vs 1칸이동한 경우
    dp[i] = max(dp[i-2], A[i-1]+ dp[i-3]) + A[i]

print(dp[n])