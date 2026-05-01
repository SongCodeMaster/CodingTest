def solution(n):
    if n == 1:
        return '수'
    
    answer = ['수']*(n)
    
    for i in range(1,n,2):
        answer[i] = '박'
    
    return ''.join(answer)