def solution(d, budget):
    if sum(d) < budget:
        return len(d)
        
    count = 0
    d.sort()

    for i in d:
        if budget < i:
            break
        budget -= i
        count += 1
        
    return count