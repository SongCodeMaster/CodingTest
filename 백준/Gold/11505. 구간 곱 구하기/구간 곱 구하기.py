# 세그먼트 트리
# 트리 초기화 -> 리프, 부모노드 초기화 -> 업데이트 , 구간곱
import sys
input = sys.stdin.readline

# 구간 곱 문제는 모듈러 연산이 필수이다.
MOD = 1000000007

n, m, k = map(int,input().split())
limit = sys.maxsize
r = 0
while 2**r < n:
    r+=1

tree_size = 2**r * 2
tree = [1] * tree_size
start_index = 2**r

# 리프노드 초기화
for i in range(start_index, start_index+n):
    tree[i] = int(input())

# 부모노드 초기화
for i in range(start_index-1,0,-1):
    tree[i] = tree[2*i] * tree[2*i + 1] % MOD

# 업데이트 (a번째를 b로 바꾸어라)
def tree_update(a,b):
    node = start_index - 1 + a
    
    # 리프노드값 변경
    tree[node] = b

    # 재 계산하면 된다 그냥
    while node > 1:
        node //= 2 # 부모 노드로 이동
        tree[node] = (tree[node*2] * tree[node*2 + 1]) % MOD

def tree_mul(a,b):
    s = start_index - 1 + a
    e = start_index - 1 + b

    my_value = 1

    while s <= e:
        if s % 2 == 1:
            my_value = (tree[s] * my_value) % MOD
            s += 1

        if e % 2 == 0:
            my_value = (tree[e] * my_value) % MOD
            e -= 1

        s = s // 2
        e = e // 2
    
    return my_value

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        tree_update(b,c)
    elif a == 2:
        print(tree_mul(b,c))