# 11399번
n = int(input())
wait_time = list(map(int, input().split()))
wait_time.sort()

sum = 0
sum_list = [0]*n

for i in range(n):
    sum += wait_time[i]
    sum_list[i] = sum


result = 0
for i in sum_list:
    result += i

print(result)