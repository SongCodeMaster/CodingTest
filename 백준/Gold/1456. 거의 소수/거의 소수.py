# 메모리가 크기때문에 소수 배열 만들어두기, 에라토스테네스의 체
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
limit = math.isqrt(m)
prime_TF = [True]*(limit+1)
prime_TF[0] = False
prime_TF[1] = False
prime_num = []

for i in range(2,limit+1):
    if prime_TF[i]:
        prime_num.append(i)
        for j in range(2*i,limit+1,i): 
            prime_TF[j] = False
count = 0

almost_prime = []

for i in prime_num:
    x = i*i
    while x <= m:
        if x >= n:
            count +=1 
        x *= i # 거듭제곱 꾸준히 해주면됨.

print(count)