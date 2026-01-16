# 답이 여러개인 경우 아무거나 출력이면 위상정렬과 관련있음.
# 두학생의 키 비교는 선행관계가 있다는것이다.
from collections import deque
n, m = map(int, input().split())

indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]

# 그래프 연결
for i in range(1,m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result=[]

# 위상 정렬
def topology_sort():
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

topology_sort()
print(*result)