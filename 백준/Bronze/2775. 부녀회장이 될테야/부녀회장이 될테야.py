T = int(input())
limit = 14
D = [[0]*(limit+1) for _ in range(limit+1)]

for i in range(limit+1):
    D[0][i] = i

# 1층 3호면
# 1층 2호 + 0층 3호?

# DP 메모리 다 채워주기 재귀식으로 
for i in range(1,limit+1):
      for j in range(1,limit+1):
           # 내 옆집(누적합) + 내 아랫집(새로운 사람)
           D[i][j] = D[i][j-1] + D[i-1][j]

# T번 반복하며 정답 출력
for _ in range(T):
    k = int(input())
    n = int(input())
    print(D[k][n])