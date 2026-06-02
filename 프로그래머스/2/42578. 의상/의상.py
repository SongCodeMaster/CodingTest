from collections import Counter

def solution(clothes):
    type_counts = Counter([kind for name, kind in clothes])
    
    answer = 1
    for count in type_counts.values():
        answer *= (count + 1) 
        
    return answer - 1