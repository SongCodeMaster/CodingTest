# 최솟값찾기 N과 M의값이 크므로 세그먼트 트리로 구현해야한다.
# 트리 초기화 -> 리프, 부모노드 채우기 -> 최솟값 구하기

import sys
input = sys.stdin.readline
limit = sys.maxsize

n, m = map(int,input().split())

# 트리 사이즈 구하기
r = 0
while 2**r < n:
    r += 1

tree_size = 2**r * 2
tree = [limit] * tree_size
start_index = 2**r

# 리프노드 채우기
for i in range(start_index, start_index + n):
    tree[i] = int(input())

# 부모노드 채우기 min으로 (0인값을 고려를 해야하는데 어떻게하지 그냥 초기화를 MAX로)
for i in range(start_index-1,0,-1):
    tree[i] = min(tree[i*2],tree[i*2 +1])

# 즉, s 2로 나눴을때 1이면 그대로 올라가고 e 나눴을때 0이면 남겨놓기(선택)
def tree_min(a,b):
    s = (start_index - 1) + a
    e = (start_index - 1) + b

    # 최솟값 임시로 저장할  변수
    part_min = limit

    while s <= e:
        # start가 오른쪽이면 나만 선택하고 오른쪽으로 이동
        if s % 2 == 1:
            part_min = min(part_min, tree[s])
            s += 1
            
        if e % 2 == 0:
            part_min = min(part_min, tree[e])
            e -= 1

        s = s // 2
        e = e // 2
    
    return part_min


for _ in range(m):
    a, b = map(int, input().split())
    print(tree_min(a,b))
    
