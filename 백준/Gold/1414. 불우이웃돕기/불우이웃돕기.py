# MST 신장트리: 에지리스트 + 유니온파인드 구현
# 다솜이가 기부가능한 랜선 최댓값 = 전체랜선 - MST 전체 가중치
# 알파벳순서대로 가중치값
import sys
sys.setrecursionlimit(10**6)
n = int(input())

# 아스키코드로 정수변환 함수
def len_char(ch):
    if ch == '0':
        return 0
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1 # a~z -> 1~26
    else:
        return ord(ch) - ord('A') + 27 # A~Z -> 27~52

edge=[]

edge_list = [[0]*n for _ in range(n)]

sum = 0
# 문자열받은것들 숫자로변환
for i in range(n):
    str = list(input())
    for j in range(n):
        a = len_char(str[j])
        sum += a
        edge_list[i][j] = a

if n == 1:
    print(sum)
    sys.exit()

# 에지리스트 구현
for i in range(n):
    for j in range(n):
        if edge_list[i][j] != 0:
            edge.append((i,j,edge_list[i][j]))

edge.sort(key= lambda x: x[2])

parent = [0]*n
for i in range(n):
    parent[i]=i

# 유니온파인드 구현
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


# 크루스칼: 노드가 n-1이 될때까지 수행된다.
cost = 0
count = 0
TF = False
for i,j,k in edge:
    if find(i) != find(j):
        union(i,j)
        cost += k
        count += 1
        if count == n-1:
            TF = True
            break

# 최대랜선길이 
if TF:
    print(sum - cost)
else:
    print(-1)
