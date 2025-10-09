def solution(participant, completion):
    dic = {}
    
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    for c in completion:
        if c in dic:
            dic[c] -= 1
    for key, val in dic.items():
        if val > 0:
            return key        
                