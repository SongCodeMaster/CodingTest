from itertools import combinations

def solution(numbers):
    answer = []
    number_list = list(combinations(numbers,2))
    
    for i in number_list:
        answer.append(sum(i))
    
    result = sorted(list(set(answer)))

    return result