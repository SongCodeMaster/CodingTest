import sys
input = sys.stdin.readline
n=int(input())
number=[0]*n

for i in range(n):
    number[i] = int(input())

number.sort()

for i in range(n):
    print(number[i])