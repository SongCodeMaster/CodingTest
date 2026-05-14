def solution(d, budget):
    d.sort()
    count = 0
    
    if sum(d) <= budget:
        return len(d)

        
    for i in range(len(d)):
        count += 1
        budget -= d[i]
        if budget == 0:
            return count
        elif budget < 0:
            return count - 1
        
        