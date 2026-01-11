import sys
import math
input = sys.stdin.readline

n, m = map(int,input().split())

result = math.gcd(n,m)
print('1'*result)