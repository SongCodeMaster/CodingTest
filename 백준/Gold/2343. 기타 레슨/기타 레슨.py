import sys
input = sys.stdin.readline
n, m = map(int,input().split())
A = list(map(int, input().split()))

# left 블루레이 최소, right 블루레이 최대
left, right = max(A), sum(A)

while left <= right:
    mid = (left + right) // 2
    sum = 0
    count = 0
    for i in range(n):
              if sum + A[i] > mid:
                     count += 1
                     sum = 0
              sum += A[i]
    
    if sum: # 마지막 남은 잔여 강의 블루레이에 넣기
           count += 1
    
    if count > m:
           left = mid + 1
    else:
           right = mid - 1
           answer = mid

print(answer)