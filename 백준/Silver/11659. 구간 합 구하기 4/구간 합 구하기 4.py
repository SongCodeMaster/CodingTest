import sys
input = sys.stdin.readline

numCount, repeatCount = map(int,input().split())
numbers = list(map(int,input().split()))

temp = 0
sumList = [0]

# 합 배열 생성
for i in numbers:
    temp += i
    sumList.append(temp)

# 구간합 계산
for j in range(repeatCount):
    start, end = map(int,input().split())
    result = sumList[end] - sumList[start-1]
    print(result)
