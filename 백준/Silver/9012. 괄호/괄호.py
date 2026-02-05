# VPS 문제, 괄호의 쌍이 맞아야 함.
# 괄호의 쌍이 맞으려면 
import sys
input = sys.stdin.readline

n = int(input())

def yes_no(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')

        elif s[i] == ')':
            if len(stack) == 0:
                return print('NO')
            stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

for i in range(n):
    x = list(input().strip())
    yes_no(x)