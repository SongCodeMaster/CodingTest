def solution(d, budget): 
    d.sort()
    answer = 0
    
    for i in range(len(d)):
        if budget < 0:
            break
        budget -= d[i]
        answer += 1
        
        
    return answer