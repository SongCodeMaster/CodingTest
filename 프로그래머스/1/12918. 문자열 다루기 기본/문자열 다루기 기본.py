def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False
        return answer
    
    if s.isdigit():
        answer = True
    else:
        return False
    
    return answer