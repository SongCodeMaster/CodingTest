import math

def solution(progresses, speeds):
    answer = []
    
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    my_day = days[0]
    count = 0
    
    for day in days:
        if day <= my_day:
            count += 1
            
        else:
            answer.append(count)
            my_day = day
            count = 1
            
    answer.append(count)
    
    return answer