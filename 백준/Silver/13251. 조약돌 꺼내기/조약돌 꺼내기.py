# 조약돌꺼내기 문제 10시30분까지
# M은 색상 N은 조약돌 K는 뽑는개수
# 각 색상의 조약돌이 몇개있는지

# 전체 뽑는 경우의수 / 같은 색 뽑을 확률들 더하기
# 18C2 / 5C2 + 6C2 + 7C2

# 5C2 = 5*4 // 2!
def combination(n,k):
    if n < k:
        return 0
    
    result = 1

    for i in range(n,n-k,-1):
        result *= i
    
    for j in range(1,k+1):
        result = result // j

    return result

M = int(input())
N = list(map(int, input().split()))
K = int(input())

# 18C2 / 5C2 + 6C2 + 7C2
# 확률계산하기

# 확률 계산
bottom = combination(sum(N),K)

# top 경우의수
top = 0
for i in range(len(N)):
    n = N[i]
    top += combination(n,K)

print(top / bottom)