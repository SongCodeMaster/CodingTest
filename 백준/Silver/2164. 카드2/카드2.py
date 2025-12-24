from collections import deque
n = int(input())

my_deque = deque()

# 덱 자료구조 만들기 
for i in range(1,n+1):
    my_deque.append(i)

while len(my_deque)> 1:
    my_deque.popleft()
    number = my_deque.popleft()
    my_deque.append(number)

print(my_deque[0])