# 대괄호 소괄호 짝찾기 끝 인덱스 확인해야하는것같은데
def yes_no(s):
    stack = []

    for i in s:

        if i == '.':
            if len(stack) == 0:
                return print('yes')
            else:
                return print('no')
        
        if i == '(':
            stack.append('(')

        elif i == '[':
            stack.append('[')

        elif i == ')':
            if len(stack) == 0:
                return print('no')

            if stack[-1] != '(':
                return print('no')

            stack.pop()

        elif i == ']':
            if len(stack) == 0:
                return print('no')
            
            if stack[-1] != '[':
                return print('no')

            stack.pop()

while True:
    line = input()
    if line == '.':
        break

    yes_no(line) # 그 줄을 함수에 전달