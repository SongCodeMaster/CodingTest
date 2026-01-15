# 유니온 파인드 대표 풀이문제
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
# 인덱스와 value값 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def check_same(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for _ in range(m):
    q, a, b= map(int,input().split())
    if q == 0:
        union(a,b)
    else:
        if check_same(a,b):
            print("YES")
        else: 
            print("NO")
