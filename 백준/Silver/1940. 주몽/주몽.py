import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = list(map(int,input().split()))
i = 0
j = n-1
numbers.sort()
count = 0
while i < j:
    result = numbers[i] + numbers[j]
    if result < m:
        i += 1
    elif result > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)
