def solution(n):
    answer = list(str(n))
    answer2 = list(map(int, answer))
    
    return answer2[::-1]