import math

M = int(input())
N = list(map(int, input().split()))
K = int(input())

total_pebbles = sum(N)
# 분모: 전체에서 K개 뽑기
bottom = math.comb(total_pebbles, K)

# 분자: 각 색깔별로 K개 뽑는 경우의 수 더하기
top = 0
for n in N:
    top += math.comb(n, K)

print(top / bottom)