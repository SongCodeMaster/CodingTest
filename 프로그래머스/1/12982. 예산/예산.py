def solution(d, budget):
    sorted_d = sorted(d)
    answer = 0
    
    for i in sorted_d:
        budget -= i
        
        if budget < 0:
            break
        
        answer+= 1
        
    return answer