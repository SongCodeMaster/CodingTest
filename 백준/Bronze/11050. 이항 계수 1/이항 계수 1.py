import sys
input = sys.stdin.readline
n, k = map(int, input().split())
res = 1

# 5 C 2면 => 5*4 / 2!
for i in range(k):
    res = res*(n-i)
for i in range(1,k+1):
    res = res//i
print(res)