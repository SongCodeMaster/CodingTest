import sys
sys.setrecursionlimit(10000)

# 소수 검사 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if is_prime(num * 10 + i):
                DFS(num * 10 + i)

n = int(input())

DFS(2)
DFS(3)
DFS(5)
DFS(7)