from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거하여 시간 복잡도 줄인다.
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop() # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    mydeque.append((now[i], i)) # 덱의 마지막위치에 현재값 저장
    # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값 제거
    # 슬라이딩 윈도우의 범위 : 왼쪽(i-L + 1) 오른쪽 (i)
    if mydeque[0][1] < i - L + 1:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')