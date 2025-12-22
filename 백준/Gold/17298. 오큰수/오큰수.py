import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
answer = [0] * n
stack = []  # 오큰수 못 찾은 인덱스 저장

for i in range(n):
    # 현재 A[i]가 스택 위에 있는 애들의 오큰수가 될 수 있으면 계속 처리
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()       # 오큰수 못 찾은 인덱스 하나 꺼내서
        answer[idx] = A[i]      # 그 인덱스의 오큰수를 현재 값으로 확정

    stack.append(i)

# 끝까지 못 찾은 애들은 -1
while stack:
    answer[stack.pop()] = -1

print(*answer)