# 설탕배달

# 첫번째로 무조건 3이 들어감 5로 바로 안나눠지는 이상
#  5로 나눠질때까지 계속 뺀다.
# 3 - 3 - 
# 3 - 5 -

import sys
n = int(input())

if n % 5 == 0:
    print(n // 5)
    sys.exit()

count = 0
result = 0

while n != 0:
    n = n - 3
    count += 1

    if n % 5 == 0:
        result = n // 5
        break

    if n < 0:
        print(-1)
        sys.exit()

print(count + result)
