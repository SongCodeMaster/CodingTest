from collections import deque
import sys

input = sys.stdin.readline

# 정수 앞에 넣기
def one(q, x):
    q.appendleft(x)

# 정수 뒤에 넣기
def two(q, x):
    q.append(x)

def three(q):
    if len(q) == 0:
        return print(-1)
    
    x = q.popleft()
    print(x)

def four(q):
    if len(q) == 0:
        return print(-1)
    
    x = q.pop()
    print(x)

def five(q):
    print(len(q))

def six(q):
    if len(q) == 0:
        print(1)
    else:
        print(0)
    
def seven(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])

def eight(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])
    
n = int(input())

q = deque()

for _ in range(n):
    line = input().split() # ['1', '2']

    u = int(line[0])

    if u == 1:
        v = int(line[1])
        one(q, v)

    elif u == 2:
        v = int(line[1])
        two(q, v)

    elif u == 3:
        three(q)
    
    elif u == 4:
        four(q)
    
    elif u == 5:
        five(q)
    
    elif u == 6:
        six(q)
    
    elif u == 7:
        seven(q)
    
    elif u == 8:
        eight(q)