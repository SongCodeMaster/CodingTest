def solution(participant, completion):
    dict = {}
    for i in participant:
        dict[i] = dict.get(i, 0) + 1
    
    for i in completion:
        dict[i] -= 1
    
    for key, value in dict.items():
        if value >= 1:
            return key
    