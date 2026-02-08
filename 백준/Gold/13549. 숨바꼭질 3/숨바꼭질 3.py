from collections import deque
# 걷고 순간이동 하기
# 탐색 경로는 3가지이다. 2의배수, +-1, 2의배수는 appendleft, 나머지는 후미에 넣기
import sys
input = sys.stdin.readline
limit = 100001
n, k = map(int, input().split())

q = deque()
q.append(n)
visited = [-1]*(limit)
visited[n] = 0

while q:
    now = q.popleft()

    if now == k:
        print(visited[now])
        break
    
    teleport = now * 2

    # 우선순위 가장높은 텔레포트 바로 덱에 넣기
    if 0 <= teleport <= limit and visited[teleport] == -1:
        visited[teleport] = visited[now]
        q.appendleft(now * 2)
    
    # 나머지는 후미에 넣기
    for next in [now - 1, now + 1]:
        if 0 <= next < limit and visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)