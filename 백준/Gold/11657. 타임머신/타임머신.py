import sys
# 타임머신
# 음수 가중치존재, 최소 시간 구해라 - 벨만포드
# 벨만포드: 거리배열, 에지리스트 완전탐색
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
distance = [INF]*(n+1)

# 그래프 에지리스트
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((a,b,c))

def bellman_ford(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            now = edge[j][0]
            next = edge[j][1]
            dist = edge[j][2]

            if distance[now] != INF and distance[now] + dist < distance[next]:
                distance[next] = distance[now] + dist
        
                if i == n-1:  # n-1번째에 값이 바뀌었다면 음수싸이클이다.
                    return True
    
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])