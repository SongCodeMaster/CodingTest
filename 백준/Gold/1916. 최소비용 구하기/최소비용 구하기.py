# 다익스트라로 구현 출발도시에서 도착 도시까지의 최소 비용을 출력하여라.
# 다익스트라: 거리정보배열, 힙큐
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
# 그래프 입력
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

# 출발점과 도착점 입력정보
start, end = map(int, input().split())

# 다익스트라 구현
def djikstra(start):
    q = []
    heapq.heappush(q,(0, start)) 
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 가중치, 노드번호

        if dist > distance[now]:
            continue

        for i in graph[now]: # 노드, 가중치
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

djikstra(start)

print(distance[end])