def solution(x, n):
    if x == 0:
        return [0]*n
    
    answer = []
    for i in range(x, x*n+x, x):
        answer.append(i)
    return answer