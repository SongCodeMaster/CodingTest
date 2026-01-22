import sys
input = sys.stdin.readline

n = int(input())
tree = {} # 딕셔너리

# 트리 데이터 저장
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left,right) # Key: root, Value: (left, right)

# 전위
def preorder(n):
    if n == '.':
        return
    print(n, end='') # 루트
    preorder(tree[n][0]) # 왼쪽
    preorder(tree[n][1]) # 오른쪽

# 중위
def inorder(n):
    if n == '.':
        return
    inorder(tree[n][0])
    print(n,end='')
    inorder(tree[n][1])

# 후위
def postorder(n):
    if n == '.':
        return
    postorder(tree[n][0])
    postorder(tree[n][1])
    print(n, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')