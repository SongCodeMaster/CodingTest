from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
q = deque()

A = list(map(int, input().split()))

# 큐에 값 넣기
for i in range(n):
    q.append((i,A[i]))

result = []

while q:
    x = q.popleft()
    result.append(x[0] + 1)

    if not q:
        break

    if x[1] > 0:
        for _ in range(x[1]-1):
            y = q.popleft()
            q.append(y)

    elif x[1] < 0:
        for _ in range((-x[1])):
            y = q.pop()
            q.appendleft(y)

print(*result)