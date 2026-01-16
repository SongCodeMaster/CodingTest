# 위상정렬로 풀어야겠다. 
from collections import deque
n = int(input())

# 건물 정보 받기
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
build_time=[0]*(n+1)
dp = [0] * (n + 1)         # 최종적으로 건물이 완성되는 시간 (결과값 저장용)

# 간선연결
for i in range(1,n+1):
    input_list = list(map(int, input().split()))
    build_time[i] = input_list[0]

    for build in input_list[1:-1]:
        graph[build].append(i)
        indegree[i] += 1

# 위상 정렬
def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = build_time[i] # 선행 없으면 자기 시간

    while q:
        v = q.popleft()

        for nxt in graph[v]:
            indegree[nxt] -= 1

            # [핵심 로직] 시간 갱신 (Dynamic Programming)
            # 다음 건물의 완성 시간 = max(기존 계산된 값, 지금 건물 완료 시간 + 다음 건물 짓는 시간)
            # 여러 선행 건물 중 '가장 늦게 끝나는 건물'을 기다려야 하기 때문에 max를 씁니다.
            dp[nxt] = max(dp[nxt], dp[v] + build_time[nxt])

            # 모든 선행 건물이 지어졌다면 큐에 추가
            if indegree[nxt] == 0:
                q.append(nxt)

topology_sort()

for i in range(1, n + 1):
    print(dp[i])