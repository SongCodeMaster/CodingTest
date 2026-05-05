def solution(t, p):
    answer = 0
    k = len(p)
    p_num = int(p)
    
    for i in range(len(t) - k + 1):
        sub = int(t[i:i+k])
        if sub <= p_num:
            answer += 1
            
    return answer