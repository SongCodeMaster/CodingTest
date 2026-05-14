def solution(s):
    if s[0] == ')':
        return False
    
    stack = []
    
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')' and len(stack) > 0:
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False