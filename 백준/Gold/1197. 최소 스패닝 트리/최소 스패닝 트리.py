# MST 기본 구현 문제
# 유니온파인드로 구현, 에지리스트 정렬하기
# 유니온파인드 리스트 초기화, 에지리스트 초기화 -> 에지리스트 정렬 -> 유니온파인드값 업데이트
# 에지리스트 튜플 확인하고 유니온파인드하며 부모노드 같을시 연결하지않기, 다를시 연결하기
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
input = sys.stdin.readline

# 에지리스트 구현 튜플로
edge = []
for _ in range(m):
    edge.append(tuple(map(int,input().split())))

# 가중치 기준으로 에지리스트 정렬시키기
edge.sort(key=lambda x: x[2])

# 유니온파인드 구현하기
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

cost=0
# 크루스칼 알고리즘
for u, v, w in edge:
    if find(u) != find(v):
        union(u, v)
        cost += w

print(cost)