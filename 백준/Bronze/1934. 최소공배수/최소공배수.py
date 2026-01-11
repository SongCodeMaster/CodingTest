# 둘이 곱한거에서 최대공약수로 나누기
import math
T = int(input())

number = []
for i in range(T):
    a, b = map(int, input().split())
    c = a*b // math.gcd(a,b)
    number.append(c)

for i in number:
    print(i)
