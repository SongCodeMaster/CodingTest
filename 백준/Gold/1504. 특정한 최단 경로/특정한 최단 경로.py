# 1 -> N, 2,3은 거쳐서 반드시 지나야하는 최단경로
import sys
import heapq
# 그래프입력
# 간선입력받고
# 다익스트라 힙큐로 구현해야한다.
# 모든경로의 최단을 알아내야 한다. 
# 1 -> x, y -> N
input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(1,e+1):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

x, y = map(int, input().split())


def djikstra(start):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q,(0, start)) # 비용, 노드번호
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) 

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

dist_1 = djikstra(1)
dist_x = djikstra(x)
dist_y = djikstra(y)
dist_n = djikstra(n)

result_1 = dist_1[x] + dist_x[y] + dist_y[n]
result_2 = dist_1[y] + dist_y[x] + dist_x[n]

result = min(result_1, result_2)

if result >= INF:
    print(-1)
else:
    print(result)