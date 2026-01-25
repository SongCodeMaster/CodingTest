# 세그먼트 트리
# a가 1인 경우에는 b번째수를 c로 업데이트 (def 업데이트)
# a가 2인 경우에는 b번째부터 c번째까지의 구간합 (def 구간합)
# 트리 초기화하기 (2^k * 2만큼)

import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

# 트리 초기화하기
r = 0
while 2**r <= n:
    r += 1

tree_len = 2**r * 2
tree = [0]*tree_len

# 리프 노드 채우기
for i in range(1,n+1):
    a = int(input())
    tree[2**r - 1 + i] = a

# 부모 노드 채우기
for i in range(1,2**r+1):
    tree[2**r - i] = tree[(2**r - i)*2] + tree[(2**r - i)*2 + 1]

# 트리 업데이트하기
def tree_update(a,b):
    start_index = 2**r
    idx = (start_index-1) + a
    diff = b - tree[idx]

    # 리프노드값 바꾸기
    tree[idx] = b

    # 부모 노드값 바꾸기
    while idx > 1:
        idx = idx // 2
        tree[idx] += diff


# 트리 구간합 구하기
# start index 나머지가 1이면 선택
# end index 나머지가 0이면 선택
# 부모노드로 올라가기
def tree_sum(a,b):
    start_index = (2**r -1) + a
    end_index = (2**r - 1) + b
    result = []

    while start_index <= end_index:
        if start_index % 2 == 1:
            result.append(tree[start_index])
            start_index = (start_index + 1) // 2
        else:
            start_index = (start_index + 1) // 2

        if end_index % 2 == 0:
            result.append(tree[end_index])
            end_index = (end_index - 1) // 2
        else:
            end_index = (end_index - 1) // 2
    
    return sum(result)

# 업데이트하기
for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        # 업데이트 호출
        tree_update(b,c)
    elif a == 2:
        # 구간합 구하기
        print(tree_sum(b,c))