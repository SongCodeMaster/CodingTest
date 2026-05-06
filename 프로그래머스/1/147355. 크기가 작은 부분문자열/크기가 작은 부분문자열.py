def solution(t, p):
    answer = 0
    p_num = int(p)
    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        my_string = int(t[i:i+p_len])
        if my_string <= p_num:
            answer += 1
    return answer