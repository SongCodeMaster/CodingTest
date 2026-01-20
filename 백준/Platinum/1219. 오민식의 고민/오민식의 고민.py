# 오민식의 고민
# 가중치가 전부 음수로 저장해야 하는. 형태이다. 즉, 벨만포드로 접근
# 즉, 가중치가 최소가 되도록 업데이트 해야하며 도착 도시에 도착할때마다 돈을 더하기?
# 만약 도착도시 도착하는게 불가능 INF면 gg, 무한히 많이 가진다 (싸이클존재한다 Gee)
import sys
input = sys.stdin.readline
n, start, end, m = map(int, input().split())

# 엣지리스트 구현
edge = []
for i in range(m):
    u, v, w = map(int, input().split())
    edge.append((u,v,w))

money = list(map(int,input().split()))

INF = -sys.maxsize
dist = [INF]*n

# 시작 노드 초기화 (시작 도시의 돈을 가지고 시작)
dist[start] = money[start]

for i in range(n+101):
        for u,v,w in edge:
            # u에 도달못하면 스킵
            if dist[u] == INF:
                continue
                
            # u가 양수 사이클에 연루된 노드(Gee)라면, v도 Gee가 됨
            if dist[u] == sys.maxsize:
                dist[v] = sys.maxsize
            
            # 일반적인 최댓값 갱신 로직: 소유 돈 - 이동비용 + 수입
            elif dist[v] < dist[u] - w + money[v]:
                dist[v] = dist[u] - w + money[v]

                # n-1번 이후에도 갱신이 일어나면 양수사이클이다.
                if i >= n - 1:
                    dist[v] = sys.maxsize

if dist[end] == INF:
    print('gg')
elif dist[end] == sys.maxsize:
    print('Gee')
else:
    print(dist[end])