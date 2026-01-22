# 트리 리프 노드의 개수를 구하여라. 삭제했을때
# 트리를 구성 -> 지우고 트리 구성 -> 리프 노드 세기 DFS?
import sys
sys.setrecursionlimit(10**6)
n = int(input())
root = -1
graph = list(map(int, input().split()))
delete_node = int(input())
tree = [[] for _ in range(n)]

if graph[delete_node] == root:
    print(0)
    sys.exit()

for i in range(n):

    if i == delete_node or graph[i] == delete_node:
        continue

    if graph[i] == -1:
        root = i
    else:
        tree[graph[i]].append(i)

visited = [False]*(n)
# 트리 구성 완료했으니 리프 노드 세기
# DFS에서 자식이 없으면 리프노드이다.
count = 0
def dfs(start):
    global count

    visited[start] = True
    
    if not tree[start]:
        count += 1
        return
    
    for i in tree[start]:
        if not visited[i]:
            dfs(i)

dfs(root)

print(count)