import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
ones = 0
zeros = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        plus.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zeros += 1
    else:
        minus.append(x)

# 정렬 
plus.sort(reverse=True) # 큰 수부터  
minus.sort() # 작은 수부터 

total = 0

# 양수처리
for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        total += plus[i] * plus[i+1]
    else:
        total += plus[i]

# 1 처리
total += ones

# 음수 처리
for i in range(0, len(minus), 2):
    if i+1 < len(minus):
        total += minus[i] * minus[i+1]
    else: # 1개 남았을때 
        if zeros == 0:  # 0이 없으면 남은 음수 더함
            total += minus[i]
        else:  # 0이 있으면 아무것도 안함
            total+=0

print(total)