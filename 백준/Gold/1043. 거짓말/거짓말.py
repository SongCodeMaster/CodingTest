# 진실 그룹 형성 -> 파티 정보로 연결(union) -> 파티 검사
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

# 진실을 아는 사람들 입력
know_true = list(map(int, input().split()))

if know_true[0] == 0:
    print(m)
    sys.exit()

parent=[i for i in range(n+1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 1. 진실 아는사람들끼리 union 연산
truth_root = know_true[1]
for i in range(2,len(know_true)):
    union(truth_root,know_true[i])

# 파티 정보를 저장해둘 리스트
parties = []

# 2. 파티 정보를 입력받고, 같은 파티에 온 사람끼리 Union
for _ in range(m):
    party = list(map(int, input().split()))
    party_size = party[0]
    party_people = party[1:]

    parties.append(party_people) # 나중에 검사를 위해 저장

    if party_size > 1:
        for i in range(len(party_people)-1):
            union(party_people[i], party_people[i+1])

# 모든 연결 끝난 후 각 파티를 검사
count=0
# 진실 그룹의 대장
truth_root = find(truth_root)

for party in parties:
    possible = True
    for person in party:
        # 파티원 중 한명이라도 진실 그룹과 부모가 같다면
        if find(person) == truth_root:
            possible = False
            break
    
    if possible:
        count += 1

print(count)
