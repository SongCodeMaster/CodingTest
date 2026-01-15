# 여행 계획 문제: 1,2,3 여행을 간다했을때 find1,2,3의 대표노드가 같으면 된다.
# 0 이면 아무것도하지말고 1이면 union하기
import sys
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

# 재귀함수로 구현한다 parent 활용해서
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

# parent활용해서 값 합친다.
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 인접행렬 입력 (각 줄에 n개)
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, n+1):
        if row[j-1] == 1:
            union(i,j)

plan = list(map(int, input().split()))
root = find(plan[0])
ok = True

for x in plan:
    if find(x) != root:
        ok = False
        break

if ok:
    print('YES')
else:
    print('NO')