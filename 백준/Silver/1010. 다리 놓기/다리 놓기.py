# 동쪽이 n 서쪽이 k
# 일반적인 조합문제이다 N이 30이다
import sys
input = sys.stdin.readline
T = int(input())

# 5C2 = 5*4 // 2!
def com(n,k):
    result = 1

    for i in range(n,n-k,-1):
        result *= i

    for j in range(1,k+1):
        result = result // j
    
    return result

for i in range(T):
    n, k = map(int, input().split())
    print(com(k, n))

