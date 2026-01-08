# 식을 최소로 만드려면 빼기 연산자 뒤 더하기 값들을 다 괄호치면 된다. 

import sys
import heapq
input = sys.stdin.readline

math = input().split('-') # '-' 기준 분리

hap = []
for i in math:
    temp = list(map(int, i.split('+')))
    hap.append(sum(temp))

a = hap[0]
b = sum(hap[1:])
result = a-b
print(result)